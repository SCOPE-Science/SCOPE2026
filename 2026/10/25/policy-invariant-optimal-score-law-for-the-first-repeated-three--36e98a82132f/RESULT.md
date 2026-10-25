# Policy-invariant optimal score law for the first repeated three-label guessing deck

## Finding
Consider a uniformly shuffled six-card deck containing exactly two cards of each of three labels. Before revealing each card, a player guesses one label, receives only correct/incorrect feedback, and chooses later guesses adaptively. Let \(S\) be the number of correct guesses after all six cards. Every strategy maximizing \(\mathbb E S\) induces **the same entire probability distribution**, even if the strategy randomizes among optimal choices:
\[
\mathbb E[z^S]=\frac{33z^2+30z^3+21z^4+5z^5+z^6}{90}.
\]
Consequently \(\mathbb E S=271/90\), \(\operatorname{Var}(S)=7469/8100\), and every expectation-optimal policy produces at least two correct guesses on every possible deck. The value of the mean was previously tabulated, rounded to four decimal places; the assertion here is the complete law and its invariance across **all** mean-optimal strategies.

## Assumptions and scope
There are exactly \(90=6!/(2!)^3\) equally likely distinct deck words. The player knows the composition and observes only whether each guess matches the current card. The player receives no extra observations about card identities. Strategies may use the entire history and randomization independent of the deck. Optimality means maximization of the *expected* total correct guesses, not a tail or variance criterion. This is a finite six-round result, not a statement for arbitrary compositions.

## Proof
Write \(\mathcal W\) for the set of 90 words. For a set \(B\subseteq\mathcal W\) of deck words consistent with a given feedback history, let \(t\in\{0,\ldots,6\}\) be the number of cards already guessed. Conditioning on that history leaves a uniform posterior on \(B\). For guess \(g\), write \(H_g=\{w\in B:w_{t+1}=g\}\) and \(N_g=B\setminus H_g\). These are precisely the two resulting feedback histories.

Let \(F(B,t)\) be the maximal sum, over all words \(w\in B\), of the conditional expected number of future correct guesses, each word counted once. The base case is \(F(B,6)=0\). Backward induction and independent continuation choices following the two possible feedback responses give
\[
F(B,t)=\max_{g\in\{1,2,3\}}\left[|H_g|+F(H_g,t+1)+F(N_g,t+1)\right].
\]
In particular, an action at a nonempty reachable history is expectation-optimal exactly when it attains this maximum; every continuation with positive conditional probability must also be optimal. Randomization cannot improve the maximum.

For each \(j\in\{0,\ldots,6-t\}\), define \(L_j(B,t)\) and \(U_j(B,t)\) as the respective smallest and largest possible **unnormalized** number of decks yielding exactly \(j\) correct *future* guesses among strategies attaining \(F(B,t)\). At \(t=6\), both coefficient vectors consist solely of \(|B|\) at degree zero. For an optimal action \(g\), the unnormalized future-score polynomial is a sum of the polynomial of \(H_g\) multiplied by \(z\), and the polynomial of \(N_g\); the continuations may be optimized independently. Therefore the exact componentwise recursions are
\[
L_j(B,t)=\min_{g\in G(B,t)}\big[L_{j-1}(H_g,t+1)+L_j(N_g,t+1)\big],
\]
\[
U_j(B,t)=\max_{g\in G(B,t)}\big[U_{j-1}(H_g,t+1)+U_j(N_g,t+1)\big],
\]
with out-of-range coefficients set to zero and \(G(B,t)\) the set of Bellman-maximizing guesses. Each recurrence follows by backward induction and includes every possible mean-optimal deterministic continuation. The coefficient-by-coefficient extrema are separately attained; this is sufficient to show uniqueness if lower and upper vectors coincide, without incorrectly assuming one policy simultaneously realizes unrelated extrema.

Represent each subset \(B\) by a 90-bit exact integer mask and compute these finite recurrences in decreasing \(t\). The accompanying standard-library-only verifier exhaustively evaluates all three actions at every visited state, memoizing 11,867 pairs \((B,t)\), including empty masks. At the root it obtains
\[
F(\mathcal W,0)=271,\quad (L_0,\ldots,L_6)=(U_0,\ldots,U_6)=(0,0,33,30,21,5,1).
\]
Since both extrema agree coefficientwise, **every** expectation-optimal deterministic policy has that polynomial; any randomized optimal policy is a mixture of such policies and inherits it. Normalization by 90 completes the claim. The exact rational moments follow by differentiating the polynomial at \(z=1\). This exhaustive recursion is a finite proof with all cases specified algorithmically; no untested inference about larger decks is involved.

## Verification
Run `python verify.py` with Python 3 (standard library only). The script enumerates the 90 distinct words, evaluates the complete Bellman and coefficient-extremum recursions, asserts the 11,867-state count and the exact polynomial, and **independently forward-simulates all 90 decks** under a deterministic Bellman-optimal policy. Its final output includes `VERIFY_OK`. All calculations use integers or exact rational fractions; no floating-point approximation supports the claim.

## Relationship to prior work
Diaconis, Graham, He, and Spiro (arXiv:2010.05059) formulated and bounded the partial-feedback game. Diaconis, Graham, and Spiro (arXiv:2012.04019, Table 2) already report the optimal mean \(3.0111\) for two copies of three labels; this mean is **not** claimed to be new. Diaconis and Graham (1981, Section 3) established the expectation recursion and examples of non-greedy optimality for related decks. Their published statements inspected here do not give the full three-label/two-copy score law or prove its invariance under *every* optimal policy. The new component is the coefficientwise min/max Bellman certificate establishing policy-invariant risk, not another calculation of the existing mean.

## Limitations
The conclusion concerns the first repeated-label deck with three distinct labels and uses exhaustive finite-state computation. It does not assert invariance for any larger deck. Historical priority remains uncertain in unpublished computational tables, dissertations, or implementations related to the 1981 and 2022 sources; a literature search cannot establish mathematical uniqueness of publication. The argument supplies a transparent finite exhaustive certificate and is not an independent human audit.

## References
1. P. Diaconis, R. Graham, X. He, S. Spiro, *Card Guessing with Partial Feedback*, arXiv:2010.05059 (first posted 2020-10-10), Combin. Probab. Comput. 31 (2022), 1–20, DOI:10.1017/S0963548321000134.
2. P. Diaconis, R. Graham, S. Spiro, *Guessing about Guessing: Practical Strategies for Card Guessing with Feedback*, arXiv:2012.04019 (2020), American Mathematical Monthly 129 (2022), 1–16, DOI:10.1080/00029890.2022.2069986.
3. P. Diaconis, R. Graham, *The Analysis of Sequential Experiments with Feedback to Subjects*, Ann. Statist. 9 (1981), 3–23, DOI:10.1214/aos/1176345329.
