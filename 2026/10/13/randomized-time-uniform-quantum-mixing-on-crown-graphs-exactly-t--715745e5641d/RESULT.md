# Randomized-time uniform quantum mixing on crown graphs: exactly two connected cases

## Finding
For every integer \(n\geq 3\), let \(\operatorname{Cr}_n\) be the crown graph obtained by deleting a perfect matching from \(K_{n,n}\). Let \(A_n\) denote its unweighted adjacency matrix, let \(U_n(t)=\exp(\mathrm{i}tA_n)\), and put \(M_n(t)_{ab}=|(U_n(t))_{ab}|^2\). Then a Borel probability distribution \(\mu\) on nonnegative observation times satisfies
\[
\int M_n(t)\,\mathrm{d}\mu(t)=\frac{J_{2n}}{2n}
\]
if and only if \(n\in\{3,4\}\).

For \(n=3\), the four times \(0,\ \pi/3,\ 2\pi/3,\ \pi\), assigned respective probabilities \(1/12,\ 1/2,\ 1/6,\ 1/4\), produce the uniform expected mixing matrix \(J_6/6\). For \(n=4\), the deterministic time \(\pi/4\) produces the uniform mixing matrix \(J_8/8\). For all \(n\ge5\), no probability distribution of observation times can produce uniform expected mixing.

## Assumptions and scope
Fix an integer \(n\ge3\). Label the two parts by \(u_1,\ldots,u_n\) and \(v_1,\ldots,v_n\). The edge \(u_iv_j\) is present exactly when \(i\ne j\). The adjacency Hamiltonian is unweighted and uses the convention \(\exp(\mathrm{i}tA_n)\); the sign of the exponent does not affect \(M_n(t)\). Observation times are real and nonnegative. Distributions may have atoms, continuous components, or mixtures of these. Uniform mixing means that every entry of the expected \(2n\)-by-\(2n\) matrix equals \(1/(2n)\), simultaneously for all starting vertices. This is not ordinary infinite-time Cesaro averaging.

## Proof
Order vertices by bipartition. Write \(B=J_n-I_n\), so that
\[
A_n=\begin{pmatrix}0&B\\B&0\end{pmatrix},\qquad
U_n(t)=\begin{pmatrix}\cos(tB)&\mathrm{i}\sin(tB)\\\mathrm{i}\sin(tB)&\cos(tB)\end{pmatrix}.
\]
The all-ones projection \(P=J_n/n\) obeys \(BP=(n-1)P\), whereas \(B(I-P)=-(I-P)\). Consequently, for \(c=\cos t\), \(d=\cos((n-1)t)\), \(s=\sin t\), and \(e=\sin((n-1)t)\),
\[
\cos(tB)=cI_n+\frac{d-c}{n}J_n,
\qquad
\sin(tB)=-sI_n+\frac{e+s}{n}J_n.
\]
There are precisely four transition-probability classes, depending on whether the start and end vertices occupy the same bipartition and whether their indices match. Their probabilities are
\[
\begin{aligned}
p_0(t)&=\frac{((n-1)c+d)^2}{n^2}&\text{(same vertex)},\\
p_1(t)&=\frac{(d-c)^2}{n^2}&\text{(other vertex in the same part)},\\
p_2(t)&=\frac{(e-(n-1)s)^2}{n^2}&\text{(matched, nonadjacent cross-part vertex)},\\
p_3(t)&=\frac{(e+s)^2}{n^2}&\text{(adjacent cross-part vertex)}.
\end{aligned}
\]
Every entry of \(M_n(t)\) belongs to one of these four classes. In particular, a uniform expected mixing matrix would require \(\mathbb E[p_j(T)]=1/(2n)\) for all \(j\in\{0,1,2,3\}\).

The two off-index probabilities obey, pointwise for every real \(t\),
\[
\begin{aligned}
p_1(t)+p_3(t)
&=\frac{(d-c)^2+(e+s)^2}{n^2}\\
&=\frac{2-2\bigl(dc-es\bigr)}{n^2}\\
&=\frac{2-2\cos(nt)}{n^2}\\
&\leq\frac4{n^2}.
\end{aligned}
\]
The identity uses \(dc-es=\cos((n-1)t)\cos t-\sin((n-1)t)\sin t=\cos(nt)\). If the expected mixing were uniform, the left-hand side would instead have expectation \(1/n\), so \(1/n\le4/n^2\), hence \(n\le4\). Thus no such distribution exists for \(n\ge5\).

When \(n=3\), the four probabilities at the times \(0,\ \pi/3,\ 2\pi/3,\ \pi\), in that order, form the exact table
\[
\begin{array}{c|cccc}
 &0&\pi/3&2\pi/3&\pi\\\hline
p_0&1&1/36&1/4&1/9\\
p_1&0&1/9&0&4/9\\
p_2&0&1/12&3/4&0\\
p_3&0&1/3&0&0
\end{array}.
\]
Multiplication by the probability vector \((1/12,1/2,1/6,1/4)\) yields \(1/6\) in each of the four rows. The graph therefore mixes uniformly in expectation under the displayed four-atom law.

When \(n=4\), set \(t=\pi/4\). Then \(c=s=1/\sqrt2\), \(d=-1/\sqrt2\), and \(e=1/\sqrt2\). Direct substitution into the four formulas gives \(p_0(t)=p_1(t)=p_2(t)=p_3(t)=1/8\), establishing instantaneous, and therefore randomized-time, uniform mixing. This proves the classification.

## Verification
The standalone file `verify.py` evaluates the four orbit probability tables using exact rational arithmetic, checks the proposed weights exactly, and independently evaluates the block-matrix entries for small instances by a numerical matrix exponential when NumPy and SciPy are available. The infinite no-go assertion is a pointwise trigonometric inequality and **does not rely** on finite numerical enumeration. To reproduce the core exact verification, run `python3 verify.py` with the standard-library Python interpreter. The optional numerical verification is disabled automatically when scientific Python libraries are unavailable.

## Relationship to prior work
Coutinho, Baptista, Godsil, Spier and Werner (2022), *Irrational quantum walks*, study continuous-time mixing and transfer, giving a quantum-walk spectral framework with primary MSC 81P68. Baptista, Coutinho and Marques (2023), *Unexpected Averages of Mixing Matrices*, define mixing matrices averaged against general observation-time distributions and establish examples for complete graphs, complete bipartite graphs, short paths and products. Their general machinery is compatible with, but does not itself provide, the four-class crown-graph bound and complete classification above. Adamczak and collaborators (2007), *Non-uniform mixing of quantum walk on cycles*, rule out instantaneous uniform mixing on the six-cycle and rule out ordinary infinite-time uniform Cesaro mixing for cycles; these results do not preclude the four-atom sampling law proved here. The identification \(\operatorname{Cr}_3\cong C_6\) and \(\operatorname{Cr}_4\cong Q_3\) explains both positive boundary cases. The hypercube's instantaneous uniform mixing was already known; it is not claimed as new.

## Limitations
The classification concerns the unweighted adjacency Hamiltonian on connected crown graphs \(\operatorname{Cr}_n\), not arbitrary weighted crowns, other graph lifts, discrete-time walks, or arbitrary measurement-and-reset dynamics. This result does not estimate minimum support size for an attaining observation law, its uniqueness, or robustness to edge-weight perturbations. The observation-time distribution can depend on \(n\). The novelty comparison is necessarily subject to the possibility of equivalent spectral convex-hull formulations elsewhere; independent validation has not been performed.

## References
1. G. Coutinho, P. Baptista, C. Godsil, C. Spier, and C. Werner, *Irrational quantum walks*, arXiv:2208.08971 (first public version, 2022-08-18). https://arxiv.org/abs/2208.08971
2. P. Baptista, G. Coutinho, and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378 (first public version, 2023-08-31). https://arxiv.org/abs/2308.16378
3. W. Adamczak, K. Andrew, L. Bergen, D. Ethier, P. Hernberg, J. Lin, and C. Tamon, *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096 (2007). https://arxiv.org/abs/0708.2096
4. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137 (2001). https://arxiv.org/abs/quant-ph/0104137
