# Sharp entropy onset at unit discrepancy for irrational binary subshifts

## Finding
Fix an irrational \(\alpha\in(0,1)\). For each \(B\ge0\), let \(X_{\alpha,B}\) consist of every bi-infinite binary sequence satisfying
\[
\left|\sum_{i=j}^{j+n-1}x_i-n\alpha\right|\le B\qquad(j\in\mathbb Z,\ n\ge1).
\]
Then the sharp phase diagram is
\[
\begin{array}{c|c|c}
\text{range of }B&X_{\alpha,B}&h_{\mathrm{top}}\\\hline
0\le B<1&\varnothing&\text{not applicable}\\
B=1&\text{minimal Sturmian shift of slope }\alpha&0\\
B>1&\text{nonminimal and aperiodic}&\ge c_{\alpha,B}\log2>0
\end{array},\qquad c_{\alpha,B}=\min\{B-1,\alpha,1-\alpha\}.
\]
Here aperiodic means that there are no periodic configurations, not that every orbit is dense. The entropy lower bound is valid for every fixed irrational slope; it is not merely an exponential census after varying the slope.

## Assumptions and scope
The alphabet is \(\{0,1\}\); the index set is all of \(\mathbb Z\); the constraints hold simultaneously for every positive interval length and starting position. Entropy uses natural logarithms. The empty shift is left without a numerical entropy assignment. A minimal Sturmian shift means the unique binary minimal subshift coding irrational circle rotation with digit frequency \(\alpha\).

For \(x\in\{0,1\}^{\mathbb Z}\) define a two-sided discrepancy-height sequence with \(T_0=0\) and \(T_b-T_a=\sum_{i=a}^{b-1}(x_i-\alpha)\) for \(a<b\). The defining condition is exactly that all pairwise differences of heights have absolute value at most \(B\); equivalently, the range of heights is at most \(B\).

## Proof
**Impossibility below one.** Since the digits are integers, \(T_k\equiv-k\alpha\pmod1\) for every integer \(k\). Irrationality makes these residues dense in the unit circle. Heights contained in a real interval of length strictly less than one cannot have residues dense in the circle. Every configuration in \(X_{\alpha,B}\) requires a height range of at most \(B\), so \(X_{\alpha,B}=\varnothing\) whenever \(B<1\).

**The unit boundary.** For every \(n\ge1\), the number \(n\alpha\) is nonintegral. An integer lying at distance at most one from it must be either \(\lfloor n\alpha\rfloor\) or \(\lceil n\alpha\rceil\). Hence any two length-\(n\) factors of a configuration in \(X_{\alpha,1}\) differ by at most one in their number of ones, i.e. the configuration is one-balanced. The interval constraint also forces uniform symbol frequency \(\alpha\), excluding eventual periodicity. The classical Morse--Hedlund characterization therefore places every such configuration in the Sturmian subshift of slope \(\alpha\). Conversely, all lower mechanical words
\[
x_i=\lfloor(i+1)\alpha+\theta\rfloor-\lfloor i\alpha+\theta\rfloor\quad(i\in\mathbb Z)
\]
satisfy \(\sum_{i=a}^{b-1}(x_i-\alpha)=\{a\alpha+\theta\}-\{b\alpha+\theta\}\), whose absolute value is strictly less than one. Their orbit closure is the full Sturmian shift; because the defining inequalities are closed, this closure lies in \(X_{\alpha,1}\). Thus equality holds. Its length-\(n\) language has \(n+1\) words and zero entropy; it is minimal.

**Independent exchanges immediately above one.** Fix \(B>1\) and any
\[
0<\varepsilon<\min\{B-1,\alpha,1-\alpha\}.
\]
Choose a lower mechanical word with arbitrary phase \(\theta\), and put \(r_i=\{i\alpha+\theta\}\) and \(S_i=\lfloor i\alpha+\theta\rfloor-i\alpha=\theta-r_i\). Then all heights \(S_i\) lie in \((\theta-1,\theta]\), and \(S_b-S_a\) is precisely the interval discrepancy. Let
\[
E_\varepsilon=\{i\in\mathbb Z:\ 1-\alpha-\varepsilon<r_i<1-\alpha\}.
\]
At each such position the mechanical word has digits \(x_ix_{i+1}=01\), since \(r_{i+1}=r_i+\alpha\in(1-\varepsilon,1)\). Two indices in \(E_\varepsilon\) cannot be consecutive because adjacent occurrences of \(01\) cannot overlap. For any subset \(F\subset E_\varepsilon\), simultaneously exchange \(01\) to \(10\) at all sites in \(F\); this defines a bi-infinite binary configuration because the affected pairs are disjoint.

Relative to the mechanical height sequence, exchanging at \(i\) changes only \(S_{i+1}\), increasing it by exactly one. That modified height is \(\theta+1-r_{i+1}\in(\theta,\theta+\varepsilon)\). All other heights remain in \((\theta-1,\theta]\). Hence every independently exchanged configuration has height range strictly below \(1+\varepsilon<B\) and belongs to \(X_{\alpha,B}\), uniformly over the choice of \(F\).

By Weyl equidistribution, \(\#(E_\varepsilon\cap[0,n-2])=\varepsilon n+o(n)\). Different subsets in this finite interval produce different length-\(n\) prefixes (take \(F\) to have no other elements). Thus
\[
\#\mathcal L_n(X_{\alpha,B})\ge2^{\varepsilon n+o(n)},\qquad
h_{\mathrm{top}}(X_{\alpha,B})\ge\varepsilon\log2.
\]
Taking the supremum over permissible \(\varepsilon\) gives the stated lower bound.

**No periodic points and failure of minimality.** If a configuration were periodic with period \(p\), its frequency of ones would be rational. But the interval inequalities make its frequency exactly \(\alpha\); contradiction. The Sturmian shift of slope \(\alpha\) is a nonempty closed shift-invariant subsystem for every \(B\ge1\). For \(B>1\) that subsystem has zero entropy, whereas the containing shift has positive entropy, so it is proper and \(X_{\alpha,B}\) is not minimal. This completes the phase diagram.

## Verification
The analytical argument covers all irrational \(\alpha\), all real \(B\ge0\), both time directions, and every interval length. The standalone script `verify.py` carries out illustrative finite-window checks for two irrational slopes and several positive corridor widths. It verifies that the independent exchanges leave every tested interval discrepancy below \(B\), that the selected sites do not overlap, and that the observed eligible-site densities track the interval length. These are finite sanity checks, not an infinite proof or an originality certificate.

To reproduce, run `python verify.py` using Python 3 with no additional dependencies. The mathematical proof does not require the script.

## Relationship to prior work
Morse and Hedlund's characterization of one-balanced irrational binary words as Sturmian already yields the zero-entropy boundary at \(B=1\); this boundary is **not** claimed as new. The older exponential enumeration of \(C\)-balanced binary words for integer \(C>1\), as reported by Berthé and Cecchi Bernales citing Lipatov, does not by itself establish a fixed irrational frequency and a positive exponential growth rate under *every* real excess \(B-1>0\). Bédaride--Berthé--Julien study balance/discrepancy in hypercubic billiard words and nonbalance on factors for dimension at least two; those results concern different objects and do not determine this binary corridor entropy transition. The new assertion is the universal quantitative onset for each fixed irrational slope at arbitrarily small relaxation and the concomitant minimality-to-nonminimality transition while periodic points remain absent.

## Limitations
No exact formula for positive entropy is established; only its sharp zero-versus-positive threshold and an explicit lower bound are proved. Nothing is asserted for rational slopes or higher alphabets. The classical one-balanced theorem and the qualitative fact that some larger-balance word families grow exponentially predate this result. A historical result about fixed-frequency binary bounded-discrepancy shifts could conceivably imply the new bound; bibliographic priority remains to be independently checked. The numerical examples are finite tests only.

## References
1. N. Bédaride, V. Berthé, A. Julien, *On balance properties of hypercubic billiard words*, arXiv:2502.18211v1 (first public 2025-02-25), Sections 1--2 and Theorem 1; https://arxiv.org/abs/2502.18211.
2. V. Berthé, P. Cecchi Bernales, *Balancedness and coboundaries in symbolic systems*, arXiv:1810.07453v1 (2018), Introduction and Section 2; https://arxiv.org/abs/1810.07453.
3. M. Morse, G. A. Hedlund, *Symbolic dynamics II: Sturmian trajectories*, American Journal of Mathematics 62 (1940), 1--42.
4. E. P. Lipatov, *A classification of binary collections and properties of homogeneity classes*, Problemy Kibernet. 39 (1982), 67--84, as cited in Reference 2.
