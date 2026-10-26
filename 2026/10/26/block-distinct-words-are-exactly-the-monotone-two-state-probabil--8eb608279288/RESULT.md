# Block-distinct words are exactly the monotone two-state probabilistic winners

## Finding
Let \(\Sigma\) be a finite alphabet with \(|\Sigma|\ge 2\), and let \(w\in\Sigma^n\), \(n\ge1\). Call \(w\) **block-distinct** if no letter occurs in two separated runs: equivalently, it has the form
\[
w=a_1^{r_1}a_2^{r_2}\cdots a_k^{r_k},\qquad r_i\ge1,\quad a_i\ne a_j\text{ for }i\ne j.
\]
A two-state probabilistic finite automaton (PFA) is **order-preserving** if its two state-probability update maps are nondecreasing for every input letter (equivalently, each update has nonnegative slope).

**Theorem.** A word \(w\) is the unique highest-acceptance-probability word in \(\Sigma^n\) for an order-preserving two-state PFA if and only if \(w\) is block-distinct. Moreover, every block-distinct \(w\) has such a witness with rational transition probabilities, deterministic initial state, one accepting state, strictly positive transition slopes for its occurring letters, and a strictly positive acceptance gap. Consequently its unrestricted probabilistic automatic complexity is exactly \(A_P(w)=2\).

This is a characterization of **order-preserving two-state witnesses**, not a characterization of arbitrary two-state PFAs: automata with negative slopes can also witness words having interleaved repeated letters.

## Assumptions and scope
A two-state PFA has a probability row vector \(\pi\), row-stochastic matrices \(P_a\) for \(a\in\Sigma\), and a \(0\)-\(1\) indicator vector for accepting states. Write \(x\in[0,1]\) for the probability of state 1, so reading letter \(a\) updates \(x\) by
\[
f_a(x)=q_a+p_a x,\quad q_a=(P_a)_{0,1},\quad p_a=(P_a)_{1,1}-(P_a)_{0,1}.
\]
Order preservation is \(p_a\ge0\). The PFA **witnesses** \(w\) if its acceptance probability is strictly greater on \(w\) than on every other word in \(\Sigma^n\). If either both or neither states accept, all probabilities are constant, so a witness for \(|\Sigma|\ge2\) must accept exactly one state. Choosing state 1 corresponds to maximizing the terminal \(x\); choosing state 0 corresponds to minimizing it.

## Proof
**Necessity (envelope rigidity).** Assume all \(f_a\) are nondecreasing. When state 1 accepts, set \(F(x)=\max_{a\in\Sigma}f_a(x)\). This function is nondecreasing. For each \(j\ge0\), the maximal possible state probability after \(j\) letters, starting at \(x_0\), is \(F^j(x_0)\). Inductively this holds because an increasing map preserves the order of possible predecessor states. It is attained by choosing at stage \(j\) a letter maximizing \(f_a\) at \(x_{j-1}=F^{j-1}(x_0)\). If the maximizing word is unique, the active letter at each visited state is unique: a tie would give two words with the same state and the same maximizing continuation.

Since \(F\) is nondecreasing, the orbit \(x_0,F(x_0),F^2(x_0),\ldots\) is monotone (nondecreasing or nonincreasing depending on its first step). Fix two distinct letters \(a,b\). The difference \(f_a-f_b\) is affine. It cannot be positive at two points of a monotone orbit and negative at a point between them, because affine interpolation preserves the inequalities. Hence a unique active letter cannot disappear and then reappear: otherwise comparison with the intervening active letter would give precisely those impossible signs. The unique maximizing word is block-distinct. When state 0 accepts, replace the upper envelope \(F\) by the nondecreasing lower envelope \(G(x)=\min_a f_a(x)\); the identical argument gives the same conclusion.

**Sufficiency (rational envelope construction).** Let \(w=a_1^{r_1}\cdots a_k^{r_k}\) be block-distinct, and put \(n=\sum_i r_i\) and \(\varepsilon=2^{-(2n+10)}\). We construct affine maps \(f_i(x)=p_i x+q_i\), a strictly increasing orbit \(0=x_0<x_1<\cdots<x_n<1/2\), and ordered crossing points \(c_1<\cdots<c_{k-1}\).

Start with \(f_1(x)=1/4+x/2\). Apply it to \(x_0=0\) for the first \(r_1\) positions. At the end of any block \(i<k\), let \(b_i=r_1+\cdots+r_i\), put
\[
c_i=\frac{x_{b_i-1}+x_{b_i}}2,\qquad f_{i+1}(x)=f_i(x)+\varepsilon(x-c_i),
\]
and apply \(f_{i+1}\) for the next \(r_{i+1}\) positions. For every unused alphabet symbol set \(f_a(x)=0\).

The construction is well-defined and the orbit increases strictly. Indeed, while \(x_{j-1}<1/2\), all previously introduced crossings lie to its left, so the active block map satisfies \(f_i(x_{j-1})\ge f_1(x_{j-1})>x_{j-1}\). To keep the orbit below \(1/2\), observe that each used map differs from \(f_1\) by at most \(n\varepsilon\) on \([0,1]\). Comparing its orbit to \(y_j=f_1^j(0)=1/2-2^{-(j+1)}\) gives \(x_j\le y_j+2n\varepsilon<1/2\) for \(j\le n\). This also proves the inductive increasing-order assertion and hence \(c_1<\cdots<c_{k-1}\).

Every used affine map sends \([0,1]\) into itself: writing
\[
p_i=1/2+(i-1)\varepsilon,\qquad q_i=1/4-\varepsilon\sum_{h<i}c_h,
\]
we have \(0<q_i<q_i+p_i<1\) and \(p_i>0\). It therefore corresponds to the legitimate two-state row-stochastic transition matrix
\[
P_{a_i}=\begin{pmatrix}1-q_i&q_i\\1-q_i-p_i&q_i+p_i\end{pmatrix}.
\]
For unused letters take the matrix with both rows \((1,0)\). The initial distribution is \((1,0)\), and only state 1 accepts.

At every orbit state \(x_{j-1}\) inside block \(i\), all earlier crossings lie strictly to the left and all later crossings strictly to the right. For \(h<i\), telescoping gives
\[
f_i(x_{j-1})-f_h(x_{j-1})=\varepsilon\sum_{t=h}^{i-1}(x_{j-1}-c_t)>0;
\]
for \(h>i\), the same calculation gives \(f_h(x_{j-1})-f_i(x_{j-1})<0\). The unused maps equal zero and are also strictly inferior. Thus the desired letter \(a_i\) is the unique maximizer of the upper envelope \(F=\max_a f_a\) at each step of the constructed orbit, and \(x_j=F(x_{j-1})\).

All used slopes are at least \(1/2\), while the unused zero map never dominates \(F\) on \([0,1]\) because \(f_1(x)>0\). Thus \(F\) is strictly increasing. A competing word with its first wrong letter has a strictly smaller current state, and subsequent updates cannot catch up to the corresponding iterates of \(F\). Therefore \(w\) is the unique maximizing word of length \(n\). Its minimum gap is positive because there are finitely many competitors. A one-state PFA cannot distinguish any two equal-length words, so \(A_P(w)=2\).

## Verification
Run `python3 CHECK.py` using Python's standard library. It constructs exact rational witnesses for 103 block profiles, directly compares 416,353 equal-length competing input words in the smaller profiles, and checks exact stochastic feasibility, strict local envelope inequalities, and the orbit bounds in additional longer profiles. The script supplies finite corroboration, while the proof above establishes the result for arbitrary finite alphabets and positive run lengths.

## Relationship to prior work
Gill (2024), Theorem 4.1, classifies two-state PFA complexity over a binary alphabet, including the two-block case \(a^r b^s\). His Section 4.4 discusses extending binary witnesses to larger ambient alphabets, but does not characterize words with three or more distinct letter blocks or order-preserving witnesses over arbitrary alphabets. Kjos-Hanssen (2026) proves the three-state universal upper bound and explicitly identifies the classification of two-state words on alphabets of at least three symbols as remaining open. The present theorem identifies a natural complete subfamily of that larger classification and gives an explicit rational construction with arbitrarily many distinct blocks.

## Limitations
This does not classify the words of complexity two for unrestricted PFAs over alphabets of size at least three; negative-slope transitions permit additional winning patterns, even over two letters. No uniform positive lower bound on the acceptance gap independent of word length is asserted. The conclusion concerns strict uniqueness among words of the **same** length, not language recognition across lengths. Historical priority outside the inspected literature is not certified.

## References
1. Kenneth Gill, *Probabilistic automatic complexity of finite strings*, arXiv:2402.13376, first submitted February 2024; Theorem 4.1 and Section 4.4. https://arxiv.org/abs/2402.13376
2. Bjørn Kjos-Hanssen, *Every string has probabilistic automatic complexity at most three*, arXiv:2607.26275, submitted July 28, 2026; Sections 4–5 and Remark 5.3. https://arxiv.org/abs/2607.26275
