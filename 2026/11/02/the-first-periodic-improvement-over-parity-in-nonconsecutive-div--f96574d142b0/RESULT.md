# The first periodic improvement over parity in nonconsecutive divisor sums

## Finding
Let \(\tau(n)\) denote the number of positive divisors of \(n\). For an integer \(m\ge1\) and a residue set \(R\subseteq\mathbb Z/m\mathbb Z\) with no two consecutive residues (including across the cyclic boundary), put
\[
\mathcal D_m(R)=\lim_{X\to\infty}\frac{1}{X\log X}\sum_{\substack{1\le n\le X\\n\bmod m\in R}}\tau(n),\qquad
\alpha(m)=\max_R\mathcal D_m(R).
\]
The limit exists for every fixed \(m,R\). The smallest modulus whose optimal periodic divisor mass strictly exceeds the even-integer benchmark \(3/4\) is exactly \(90\):
\[
\alpha(m)\le\frac34\quad(1\le m<90),\qquad
\alpha(90)=\frac{34}{45}=\frac34+\frac1{180}.
\]
At \(m=90\) an optimal residue set is all the even residues except \(44,46\), together with the odd residue \(45\). Its integer progression is nonconsecutive and satisfies
\[
\sum_{\substack{1\le n\le X\\n\bmod90\in R}}\tau(n)
=\frac{34}{45}X\log X+o(X\log X).
\]
This is a finite-modulus extremal statement, not a bound on unrestricted nonconsecutive selections.

## Assumptions and scope
All moduli are fixed positive integers. A cyclically independent set \(R\) obeys \(r\in R\Rightarrow r+1\notin R\), with addition modulo \(m\). In particular \(R=\varnothing\) for \(m=1\). For a fixed modulus write \(m=\prod_{p^a\parallel m}p^a\). All logarithms are natural.

## Proof
**Residue weights.** For every \(m\ge1\) and \(0\le r<m\), one has
\[
\sum_{\substack{n\le X\\n\equiv r\pmod m}}\tau(n)
=w_m(r)X\log X+o_m(X\log X),\qquad
w_m(r)=\prod_{p^a\parallel m} w_{p^a}(r),
\]
where, if \(e=\nu_p(r)<a\),
\[
w_{p^a}(r)=\frac{(e+1)(p-1)}{p^{a+1}},\qquad
w_{p^a}(0)=\frac{(a+1)p-a}{p^{a+1}}.
\]
Here \(r=0\pmod{p^a}\) in the second formula. To prove this, start with the standard divisor-sum asymptotic on residue classes coprime to a fixed modulus \(L\): each invertible class contributes
\[
\frac{1}{\varphi(L)}\prod_{p\mid L}(1-p^{-1})^2\,X\log X+o_L(X\log X).
\]
This follows from \(\tau=1*1\), Dirichlet's hyperbola method, and character orthogonality: the principal character has a double pole of leading coefficient \(\prod_{p\mid L}(1-p^{-1})^2\) at \(s=1\), while nonprincipal characters have no double pole. More elementarily, summing characters over intervals gives the same error-saving for each fixed \(L\).

For \(p^a\), condition on \(\nu_p(n)=e<a\). Dividing by \(p^e\) leaves one invertible residue modulo \(p^{a-e}\); multiplicativity of \(\tau\) contributes \(e+1\), giving
\[
\frac{e+1}{p^e}\frac{(1-p^{-1})^2}{\varphi(p^{a-e})}
=\frac{(e+1)(p-1)}{p^{a+1}}.
\]
When the residue is zero, sum the geometric tail over \(e\ge a\):
\[
(1-p^{-1})^2\sum_{e=a}^{\infty}\frac{e+1}{p^e}
=\frac{(a+1)p-a}{p^{a+1}}.
\]
The Chinese remainder theorem and the same character argument applied simultaneously at all primes show the stated product formula. The tail in \(e\) is absolutely summable, so the limiting passage is justified. These weights sum to one over all residue classes, and \(\mathcal D_m(R)=\sum_{r\in R}w_m(r)\).

**Integer reduction.** Define
\[
L_m=\prod_{p^a\parallel m}p^{a+1},\qquad W_m(r)=L_m w_m(r)\in\mathbb Z_{>0}
\]
for \(m\ge2\), with \(L_1=W_1(0)=1\). Explicitly, each prime-power factor in \(W_m(r)\) is \((e+1)(p-1)\) for \(e<a\), or \((a+1)p-a\) when \(r=0\pmod{p^a}\). It suffices to maximize the *integer* sum \(\sum_{r\in R}W_m(r)\) over independent sets of the cycle.

For each first-vertex choice \(f\in\{0,1\}\), let \(D_i(b)\) be the greatest weight among subsets of the path \(0,\ldots,i\) with indicator at \(0\) equal to \(f\) and indicator at \(i\) equal to \(b\). Invalid states have value \(-\infty\). Initialize \(D_0(f)=fW_m(0)\) and then use, for \(i\ge1\),
\[
D_i(0)=\max(D_{i-1}(0),D_{i-1}(1)),\quad
D_i(1)=W_m(i)+D_{i-1}(0).
\]
Forbid the terminal choice \(b=f=1\) to close the cycle. Maximizing over \(f,b\) is *exactly* the cyclic independent-set optimum by induction on the path length. At \(m=1\) only the empty set is admissible.

**Exhaustion of the first crossing.** Applying this integer recurrence separately for every \(m=1,\ldots,90\) yields \(4\max_R\sum_{r\in R}W_m(r)\le3L_m\) for every \(m<90\), and precisely \(L_{90}=2700\) and optimum \(2040\) at \(m=90\). Complete exact integer results are in `artifacts/values_through_90.tsv`; `artifacts/verify.py` computes each entry from prime factorizations, runs the recurrence, and cross-checks it by independent subset enumeration for \(1\le m\le15\). The recurrence proves exhaustive optimality without a numerical tolerance or heuristic search.

For transparency, the simple even-residue set has numerator \(2025\) over denominator \(2700\) at modulus \(90\). Replacing even residues \(44\) and \(46\) (each weight \(24\)) by their common odd neighbor \(45\) (weight \(63\)) raises the numerator by \(15\), reaching \(2040/2700=34/45\). The replacement preserves the cyclic nonadjacency condition. This gives the matching explicit lower bound and completes the proof.

## Verification
From the self-contained source `artifacts/verify.py`, run `python3 artifacts/verify.py` in the directory containing the files. It validates normalization of all CRT weights, all \(90\) exact integer dynamic programs, a separate brute-force independent-set enumeration for moduli at most \(15\), the first threshold, the witness, and the recorded table. The execution output is included in `artifacts/verification_output.txt`. All finite checks are exhaustive by the proved dynamic-program recurrence. They do not replace the infinite analytic residue-weight lemma.

## Relationship to prior work
Chatterjee, *Divisor Sums with Spacing Constraints* (first public arXiv version dated 2026-10-22), studies unrestricted finite nonconsecutive subsets and much larger growing separation parameters. The paper proves asymptotic results for the unrestricted optimum and employs independence graphs, but its inspected text does not state the arithmetic optimization over **fixed periodic residue classes**, the exact first modulus, or the specific \(34/45\) optimum. Standard divisor-sum asymptotics in arithmetic progressions supply the local weights; ordinary maximum-weight independent-set dynamic programming supplies the finite optimization. Neither ingredient alone reports the arithmetic first-crossing result. Searches for equivalences and stronger coverage are summarized in `AUDIT.json`. Previously known unrestricted results imply only an upper bound of coefficient one, not this exact periodic threshold.

## Limitations
The theorem is confined to periodic selectors with period at most \(90\) for the minimality assertion, and gives the exact optimum at \(90\). It does not classify all higher moduli or all optimal residue sets, and it does not estimate the unrestricted optimizer beyond cited work. The asymptotic concerns fixed moduli; no uniformity in growing \(m\) is claimed. Literature searches do not prove historical uniqueness, and independent priority review remains open.

## References
- A. Chatterjee, *Divisor Sums with Spacing Constraints*, arXiv:2610.31832v1 (2026-10-22), https://arxiv.org/abs/2610.31832 . Full HTML text inspected.
- Classical Dirichlet divisor summatory formula and divisor sums in fixed arithmetic progressions, obtained from Dirichlet characters and the Dirichlet hyperbola method.
- Standard path/cycle maximum-weight independent-set dynamic programming (recurrence proved above).
