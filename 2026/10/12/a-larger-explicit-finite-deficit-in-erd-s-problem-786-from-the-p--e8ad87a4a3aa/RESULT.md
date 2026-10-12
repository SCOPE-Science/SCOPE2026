# A larger explicit finite deficit in Erdős Problem 786 from the published proof constants
## Finding
Call \(A\subseteq\{1,\ldots,N\}\) admissible if equality of the products of two finite subsets of \(A\) forces the two subsets to have the same cardinality. Li's Theorem 2 proves a uniform finite-density gap with the explicit choice \(\eta=e^{-5000}\) for \(N\ge e^{200000}\). Keeping the proof, the parameters
\[
P=N^{1/32},\qquad M=\lceil4(\log N)^2\rceil,\qquad c_0=e^{-1400},\qquad p_0=e^{3200},
\]
and every auxiliary lemma unchanged, one may instead take
\[
\eta_0=\frac{e^{-3200}}{5}.
\]
Precisely, for every \(N\ge e^{200000}\) and every admissible \(A\subseteq\{1,\ldots,N\}\),
\[
|A|<(1-\eta_0)N.
\]
This is an improvement by the factor \(e^{1800}/5\) in the explicit deficit furnished by the same proof.

## Assumptions and scope
All terminology and auxiliary estimates are those of Section 4 of arXiv:2609.37471v1. Put \(E=\{1,\ldots,N\}\setminus A\), \(D=|E|\), and \(\delta=D/N\). The argument below assumes \(\delta\le\eta_0\) and derives that \(A\) is not admissible. Therefore an admissible set must satisfy the displayed strict size bound.

The claim is only an extraction of stronger explicit constants from the published proof. It does not change Li's asymptotic method, does not approach the conjectural optimal deficit \(0.1715\ldots\), and does not claim that \(\eta_0\) is optimal even within that proof architecture.

## Proof
Li calls a prime heavy when \(|E\cap p\mathbb N|\ge N/(16p)\), writes \(S\) for the sum of \(1/p\) over heavy primes, and proves in Lemma 7 that
\[
S\le3072\delta.
\]
Since \(\delta\le\eta_0\),
\[
S+\delta\le3073\eta_0
 =\frac{3073}{5}e^{-3200}
 <\frac12e^{-1400}=\frac{c_0}2.
\]
The strict inequality is immediate, for example, from \(e^{1800}>2^{1800}>2\cdot3073/5\). Thus every later use of \(S+\eta<c_0/2\) in the published proof remains valid with \(\eta_0\).

The only displayed place where the much smaller choice \(e^{-5000}\) is needed for a different scale is Step 4. For a prime \(p\le p_0=e^{3200}\), the number of \(p\)-pairs in \(A\) is at least
\[
\left\lfloor\frac Np\right\rfloor-2D
\ge \frac N{p_0}-1-2\eta_0N.
\]
Because \(N\ge e^{200000}\),
\[
\frac1N+2\eta_0
\le e^{-200000}+\frac25e^{-3200}
<\frac12e^{-3200}=\frac1{2p_0}.
\]
Indeed, after division by \(e^{-3200}\), this is \(e^{-196800}+2/5<1/2\), and \(e^{196800}>10\). Hence
\[
\left\lfloor\frac Np\right\rfloor-2D\ge\frac N{2p_0}.
\]
Li's Lemma 4 then gives a matching of size at least \(N/(4p_0)\), exactly the input used to declare every \(p\le p_0\) rich. The subsequent comparison \(N/(4p_0)\ge M\) depends only on \(N\ge e^{200000}\) and is unchanged.

In Lemma 10 the source takes \(\gamma=c_0/2\). The preceding heavy-prime inequality gives the same lower bound for the relevant set of smooth replacements. Its third failure probability is bounded by
\[
\frac{4\delta}\gamma=\frac{8\delta}{c_0}
\le\frac85e^{-1800}<\frac18.
\]
The other two failure probabilities remain at most \(1/10\) and \(1/8\), so the success probability is still greater than \(1/2\). All later word-length estimates are independent of \(\eta\).

Finally, Step 7 starts with at least \(c_0N\) smooth integers and discards at most \(NS+D\) of them. Since \(S+\delta<c_0/2\), at least \(c_0N/2>0\) candidates remain. The rest of Li's lifting argument is unchanged and contradicts admissibility. Therefore \(\delta>\eta_0\), which is equivalent to
\[
|A|<(1-\eta_0)N.
\]

## Verification
The standalone script `verify.py` checks the three numerical inequalities on which the stronger constant depends after scaling away the enormous exponentials: the heavy-prime slack, the small-prime pair count, and the coupling failure bound. It also checks that the improvement factor over \(e^{-5000}\) is \(e^{1800}/5\).

Replay command: `python verify.py`

Expected output begins with `VERIFY_OK` and reports positive margins for all three constraints. The script is a consistency check; the proof above establishes the inequalities for all \(N\ge e^{200000}\) and all \(\delta\le\eta_0\).

## Relationship to prior work
Li's Theorem 2 states that one may take \(\eta=e^{-5000}\) for \(N\ge e^{200000}\), and explicitly says no attempt is made to optimize \(\eta\). Section 4 gives the constants \(c_0=e^{-1400}\), \(p_0=e^{3200}\), the heavy-prime estimate, the small-prime richness step, and the coupling bound used above.

Gessel's September 2026 note proves a natural-density bound \(\delta\le7/8\) for infinite admissible sets but explicitly does not settle the finite-set question where the set may vary with \(N\). The repetition-allowed theorems of Erdős--Ruzsa--Sárközy and Granville--Soundararajan apply to a stronger condition and therefore do not supply this finite distinct-factor constant.

Targeted searches for the source identifier, the explicit constants \(e^{-5000}\), \(e^{-1400}\), and finite distinct-factor deficit improvements found no checked statement of \(e^{-3200}/5\) or a stronger explicit constant for the same theorem. The result is therefore a quantitative sharpening of the newly published finite distinct-factor theorem, not a claim about the optimal density gap.

## Limitations
The constant remains astronomically smaller than the conjectural deficit \(0.1715\ldots\). It is not claimed optimal. The argument depends on Li's Lemmas 3, 4, 7--11 and their stated constants; it only rechecks every place in Section 4 where the deficit parameter is used. No independent formal verification of the strengthened constant is supplied.

## References
1. Shisheng Li, *A negative answer to Erdős Problem #786*, arXiv:2609.37471v1, 2026; especially Theorem 2 and Section 4.
2. Declan Gessel, *Erdős 786(i): an elementary density obstruction for distinct-factor product sets*, research note, September 6, 2026.
3. T. F. Bloom, *Erdős Problem #786*, Erdős Problems database.
4. P. Erdős, I. Z. Ruzsa, A. Sárközy, *On the number of solutions of \(f(n)=a\) for additive functions*, Acta Arith. 24 (1973), 1--9.
5. A. Granville, K. Soundararajan, *The spectrum of multiplicative functions*, Ann. of Math. 153 (2001), 407--470.
