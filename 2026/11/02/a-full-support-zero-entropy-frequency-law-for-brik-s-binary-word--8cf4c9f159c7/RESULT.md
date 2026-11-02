# A full-support zero-entropy frequency law for Brik's binary word

## Finding

Let \(B_1=101\), let \(B_{i+1}=B_iB_i[i+1..|B_i|]\) for \(i\geq1\), with positions indexed from one, and let \(\mathbf b\) be the common infinite extension. For a nonempty finite word \(u\), let \(F_u(N)\) be the number of occurrences of \(u\) beginning at positions \(1,\ldots,N\) of \(\mathbf b\). Then every cylinder frequency
\[
\mu(u)=\lim_{N\to\infty}\frac{F_u(N)}{N}
\]
exists. It is positive exactly for words avoiding \(00\); for words containing \(00\), it is zero. For each fixed \(u\),
\[
F_u(N)=\mu(u)N+O_u((1+\log N)^2).
\]
The cylinder frequencies define an invariant Borel probability measure \(\mu\) on the one-sided golden-mean shift \(X=\{x\in\{0,1\}^{\mathbb N}:00\text{ never occurs}\}\). Its support is all of \(X\), but its Kolmogorov--Sinai entropy is zero:
\[
\boxed{\operatorname{supp}\mu=X,\qquad h_\mu(\sigma)=0<h_{\mathrm{top}}(X)=\log_2\varphi},
\]
where \(\varphi=(1+\sqrt5)/2\) and entropy is measured in bits per symbol. Thus \(\mathbf b\) is a generic point for a fully supported zero-entropy invariant measure on a positive-topological-entropy shift.

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\), with the displayed unmodified recursion; \(B_i[i+1..|B_i|]\) denotes the suffix obtained by removing its first \(i\) symbols. Prefixes and factors are contiguous, with overlaps counted. The infinite word is well defined because \(B_i\) is a prefix of \(B_{i+1}\). The frequency \(\mu(u)\) uses starting positions, including starts whose length-\(|u|\) windows extend beyond the first \(N\) symbols. The shift is one-sided and \(\sigma\) is the left shift. Entropy \(h_\mu(\sigma)\) is \(\lim_{m\to\infty}H_m(\mu)/m\), where \(H_m=-\sum_{|u|=m}\mu(u)\log_2\mu(u)\). No ergodicity or uniqueness of invariant measure is asserted.

Two established properties from Shallit (2026) are used: the exact length \(\ell_i=|B_i|=2^{i-1}+i+1\), and the assertions that \(\mathbf b\) is recurrent and that its language consists of all finite binary words avoiding \(00\). Those source statements were read in their original full text (Proposition 1, Theorems 3 and 7). The new proof independently establishes all frequency and entropy assertions from the displayed recursion and those properties.

## Proof

**1. Convergence at recursive lengths.** Fix a nonempty word \(u\) of length \(m\), and write \(N_i=N_i(u)\) for its number of occurrences wholly inside \(B_i\). Concatenating \(B_i\) and its suffix \(B_i[i+1..\ell_i]\) retains all the occurrences in the first copy and all occurrences in the second copy except those beginning in the first \(i\) positions of \(B_i\). It may add at most \(m-1\) occurrences crossing the join. Hence, exactly,
\[
N_{i+1}=2N_i-D_i+J_i,\qquad 0\le D_i\le i,\quad 0\le J_i\le m-1.
\]
Therefore \(|N_{i+1}-2N_i|\le i+m-1\), and the ratios \(N_i/2^{i-1}\) converge to a number \(\mu(u)\in[0,1]\), since
\[
\sum_{i\geq1}\frac{i+m-1}{2^i}<\infty.
\]
The explicit tail estimate gives, for every \(i\geq1\),
\[
\left|N_i-2^{i-1}\mu(u)\right|\le i+m,
\qquad
\left|N_i-\ell_i\mu(u)\right|\le2i+m+1.
\tag{1}
\]
The second inequality uses \(\mu(u)\le1\) and the exact length formula. In particular the frequency at the recursive-length prefixes converges, with an effective exponential-in-\(i\) error bound.

**2. All prefix lengths, and discrepancy.** Let \(F(N)=F_u(N)\). A factor beginning in one of the last \(m-1\) positions of \(B_i\) might extend beyond \(B_i\), whence \(|F(\ell_i)-N_i|\le m-1\). Write an arbitrary sufficiently large \(N\) as \(N=\ell_i+t\), \(0\le t<\ell_{i+1}-\ell_i=\ell_i-i\). The appended segment of \(B_{i+1}\) is \(\mathbf b[i+1..\ell_i]\). Comparing length-\(m\) windows beginning in the first \(t\) positions of that appended segment with the windows beginning at positions \(i+1,\ldots,i+t\) of \(\mathbf b\), at most \(m-1\) windows near its right boundary need differ. Thus
\[
F(\ell_i+t)=F(\ell_i)+F(i+t)-F(i)+\varepsilon_{i,t},
\qquad |\varepsilon_{i,t}|\le m-1.
\tag{2}
\]
Put \(E(N)=F(N)-\mu(u)N\). By (1), \(E(\ell_i)=O_u(i+1)\); trivially \(|E(i)|\le i\). Equation (2) yields
\[
|E(N)|\le |E(i+t)|+O_u(i+1).
\tag{3}
\]
For this decomposition \(i=O(1+\log N)\) and
\[
\frac{i+t}{N}\le\frac{\ell_i}{2\ell_i-i}\le\frac34.
\]
Iterating (3) until the argument is bounded therefore takes \(O(\log N)\) steps, each costing \(O_u(1+\log N)\). This proves \(E(N)=O_u((1+\log N)^2)\), in particular \(F(N)/N\to\mu(u)\). Since frequencies are limits of empirical cylinders of the single infinite word, they satisfy the nonnegative consistency and stationarity equations and determine a \(\sigma\)-invariant Borel probability measure.

**3. Strict positivity of every occurring factor.** The source's recurrence theorem ensures that each factor \(u\) occurs at arbitrarily large starting positions \(p\). Fix such an occurrence and take \(J\) minimal with \(\ell_J\ge p+m-1\). As \(p\to\infty\), \(J=O(\log(p+m))\), so choose \(p\) with \(p>J\) and \(2^{p-J}>p+1\). Until stage \(p\), every descendant of this particular occurrence has starting position at least \(p\). Thus, for stages \(i=J,\ldots,p-1\), it survives both copies in the recursion, because the second copy removes only the first \(i<p\) starting positions. Distinct left/right descendants give
\[
N_p\ge2^{p-J}>p+1.
\]
For every \(i\ge p\), the bound \(N_{i+1}\ge2N_i-i\) from Step 1 implies
\[
\mu(u)\ge\frac{N_p}{2^{p-1}}-\sum_{i=p}^{\infty}\frac{i}{2^i}
=\frac{N_p-(p+1)}{2^{p-1}}>0.
\]
For any word containing \(00\), \(N_i=0\) identically by the source's factor-language theorem. Therefore \(\mu(u)>0\) precisely for allowed golden-mean words, proving \(\operatorname{supp}\mu=X\). Shallit's full-language theorem also gives \(h_{\rm top}(X)=\log_2\varphi\), since the number of allowed length-\(m\) words is the Fibonacci number \(F_{m+2}\).

**4. Zero measure-theoretic entropy.** Fix an integer \(j\ge1\). For every \(I\ge j\), the recursion exhibits \(B_I\) as a subsequence (obtained by deleting symbols while preserving order) of the periodic template \(B_j^{2^{I-j}}\): this follows by induction, since \(B_{i+1}\) consists of one copy of \(B_i\) and another copy with the first \(i\) symbols deleted. The number of removed template symbols is exactly
\[
L_{j,I}=2^{I-j}\ell_j-\ell_I=2^{I-j}(j+1)-I-1,
\qquad
\lim_{I\to\infty}\frac{L_{j,I}}{\ell_I}=\delta_j:=\frac{j+1}{2^{j-1}}.
\tag{4}
\]
Among length-\(m\) windows wholly inside \(B_I\), call a window *good* if its \(m\) retained positions are consecutive in the template. Each template deletion spoils at most \(m\) starting windows, so at most \(mL_{j,I}\) windows are bad. Every good window is a length-\(m\) cyclic factor of \(B_j\); the set \(G_{j,m}\) of such words has cardinality at most \(\ell_j\). Thus the limiting cylinder distribution assigns mass at most \(m\delta_j\) to \(G_{j,m}^{\mathsf c}\).

Partitioning the length-\(m\) random word according to membership in \(G_{j,m}\), and using the binary entropy bound \(H_2(p)\le1\), gives
\[
H_m(\mu)\le1+\log_2\ell_j+m\min\{1,m\delta_j\}.
\tag{5}
\]
Choose \(m_j=2^{\lfloor j/2\rfloor}\). Then \((1+\log_2\ell_j)/m_j\to0\) and \(m_j\delta_j\to0\), so (5) proves \(H_{m_j}(\mu)/m_j\to0\). By stationarity, block entropies are subadditive and their asymptotic per-symbol limit exists as the infimum; hence \(h_\mu(\sigma)=0\). This completes the proof.

## Verification

The accompanying standard-library Python program `verify.py` reconstructs \(B_i\), checks the exact length formula, the \(00\)-avoidance and the two-sided factor-count recurrence \(-i\le N_{i+1}-2N_i\le m-1\) on nine representative factors through level 21; it also checks finite subsequence embeddings and their exact deletion deficits for several base and terminal levels. Recorded executable output is in `verification_output.txt`. For illustration, the frequency of \(1111\) among complete windows is near \(0.00024414\) by level 21; this is not asserted to equal that decimal exactly. The infinite positivity, discrepancy and entropy conclusions follow from the proof, not from the finite computations.

## Relationship to prior work

Shallit, *Brik's sequence: a strange recursion* (2026, arXiv:2605.07542v1), introduced and studied the same word. Proposition 1 determines the lengths; Theorems 3 and 7 determine recurrence and the complete factor language; Theorem 10 proves the frequency only of individual ones (and Theorem 12 its transcendence). The present result instead obtains convergence and positivity of the entire cylinder-frequency family, a quantified uniform-prefix discrepancy, and the zero metric entropy of the resulting full-support measure. These assertions do not follow from just letter density or knowledge of the factor language: positive topological entropy does not determine the entropy of a particular invariant measure. Results about rank-one symbolic systems and finite symbolic rank offer related zero-entropy mechanisms, but the cited standard rank-one bounded-spacer frameworks do not identify or establish these assertions for the prefix-deletion recursion; the proof here is direct via a deletion-template argument. The general prior work of Gao and Ziegler (2019) is contextual, not credited with these new assertions.

## Limitations

The theorem concerns only the precise Brik recursion, not arbitrary prefix-deletion schemes. It does not show that \(\mu\) is ergodic, mixing, a unique invariant measure on \(X\), or a measure of maximal entropy; the latter is ruled out by the entropy computation. Positive cylinder frequency can be extremely small and does not imply bounded gaps or uniform recurrence. The all-cylinder discrepancy constants depend on the fixed factor. Exhaustive publication priority and independent mathematical review remain outstanding.

## References

1. J. Shallit, *Brik's sequence: a strange recursion*, arXiv:2605.07542v1, first submitted 2026-05-08, https://arxiv.org/html/2605.07542 (read complete body, particularly Proposition 1 and Theorems 3, 7, 10).
2. S. Gao and C. Ziegler, *Topological mixing properties of rank-one subshifts*, Transactions of the London Mathematical Society 6 (2019), 1--21, https://doi.org/10.1112/tlm3.12016 (related symbolic-dynamics context; no implication used).
