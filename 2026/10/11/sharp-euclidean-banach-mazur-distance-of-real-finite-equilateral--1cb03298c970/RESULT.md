# Sharp Euclidean Banach--Mazur distance of real finite equilateral Lipschitz-free spaces

## Finding
For every integer \(m\ge2\), let \(M_m\) be an \(m\)-point metric space whose distinct points are a common positive distance apart. Its real Lipschitz-free space has dimension \(m-1\). The exact *multiplicative* Banach--Mazur distance from that space to a real Euclidean space is
\[
 d_{\mathrm{BM}}\bigl(\mathcal F(M_m),\ell_2^{m-1}(\mathbb R)\bigr)^2
 =\frac{2}{m}\left\lfloor\frac{m^2}{4}\right\rfloor
 =\begin{cases}
 \frac m2,&m\text{ even},\\[2pt]
 \frac{m^2-1}{2m},&m\text{ odd}.
 \end{cases}
\]
An optimal Euclidean comparison on the *dual* Lipschitz space is given by the usual centered-coordinate quadratic form. The formula includes the exact parity dependence and the asymptotic order \(\sqrt{m/2}\).

## Assumptions and scope
Throughout, scalars are **real**, \(m\) is an integer at least two, and all nonzero distances of \(M_m\) are equal. A common positive distance is irrelevant because it scales the Lipschitz norm uniformly. We normalize it to one. For normed spaces of equal finite dimension, \(d_{\mathrm{BM}}(X,Y)=\inf_T\|T\|\|T^{-1}\|\), the infimum being over invertible linear maps. By finite-dimensional duality, \(d_{\mathrm{BM}}(X,Y)=d_{\mathrm{BM}}(X^*,Y^*)\).

Identify the dual Lipschitz space with
\[
 H_m=\{f\in\mathbb R^m:\sum_{i=1}^m f_i=0\},\qquad
 N(f)=\max_i f_i-\min_i f_i.
\]
Indeed, a function on an equilateral metric space is determined modulo constants and its Lipschitz seminorm is exactly its coordinate oscillation. Put \(Q(f)=\sum_i f_i^2\) on \(H_m\).

## Proof
**1. Reduction of all Euclidean comparisons to one quadratic form.** A Hilbertian norm on \(H_m\) is \(\sqrt{Q_1}\) for a positive-definite quadratic form \(Q_1\). If its distortion relative to \(N\) is at most \(D\), scale \(Q_1\) so that
\[
N(f)^2\le Q_1(f)\le D^2N(f)^2\quad\text{for all }f\in H_m.
\]
Permutations of the \(m\) coordinates preserve both \(H_m\) and \(N\). Average \(Q_1\) over all coordinate permutations. The resulting positive-definite form satisfies the same inequalities and is permutation invariant. A permutation-invariant symmetric matrix on \(\mathbb R^m\) has a constant diagonal and a constant off-diagonal; when restricted to \(H_m\), its quadratic form is \(c\sum_i f_i^2=cQ(f)\) for some \(c>0\). Thus no Euclidean norm gives smaller distortion than a scaled version of \(\sqrt Q\), which therefore attains the optimum.

**2. Smallest centered sum of squares at unit oscillation.** If \(N(f)=1\), choose indices \(i,j\) with \(f_i-f_j=1\). Since \(\sum_k f_k=0\),
\[
Q(f)\ge f_i^2+f_j^2\ge\tfrac12(f_i-f_j)^2=\tfrac12.
\]
Equality is attained by the vector with two entries \(+1/2\) and \(-1/2\) and all remaining entries zero. Thus \(\min_{N(f)=1}Q(f)=1/2\).

**3. Largest centered sum of squares at unit oscillation.** Add a common constant so that the smallest coordinate is zero and the largest is one. This does not change \(N\) or \(Q\) when \(Q\) is understood as the centered sum of squares. Writing the translated entries as \(u_i\in[0,1]\),
\[
Q(f)=\sum_{i=1}^m u_i^2-\frac1m\Big(\sum_{i=1}^m u_i\Big)^2.
\]
This is a convex function on the cube, so its maximum occurs at a vertex. At a vertex with exactly \(k\) entries equal to one, its value is \(k(m-k)/m\). Consequently
\[
\max_{N(f)=1}Q(f)=\frac1m\max_{0\le k\le m}k(m-k)
=\frac1m\left\lfloor\frac{m^2}{4}\right\rfloor.
\]
The maximizing binary vectors have the two population counts as balanced as possible.

**4. Optimal distortion.** For the Euclidean norm \(\sqrt{Q}\), the square of its norm-distortion relative to \(N\) is
\[
\frac{\max_{N(f)=1}Q(f)}{\min_{N(f)=1}Q(f)}
=\frac{2}{m}\left\lfloor\frac{m^2}{4}\right\rfloor.
\]
The averaging step shows this value is a lower bound for **every** Euclidean comparison, not only for a specified coordinate embedding. Finally use \(d_{\mathrm{BM}}(X,Y)=d_{\mathrm{BM}}(X^*,Y^*)\) with \(X=\mathcal F(M_m)\) and \(Y\) Euclidean. This proves the stated result for all integers \(m\ge2\). \(\square\)

## Verification
Run `python3 verify.py` with the Python standard library from the same directory as this document. The verifier uses exact rational arithmetic. It checks the binary maximizing family for every \(2\le m\le16\), exact lower-bound witnesses, all nonconstant coordinate vectors from the ternary grid \(\{0,1/2,1\}^m\) for \(2\le m\le8\), and the pairwise variance identity. Its successful output is `EQUILATERAL_EUCLIDEAN_EXACT_OK 9966`. No finite calculation is used as a proof of the unbounded-dimensional theorem; that proof is in the preceding section.

## Relationship to prior work
Godard (2009, §3) gives an exact real Lipschitz-free norm for arbitrary finite discrete equilateral spaces, which supplies the underlying metric-space model; that prior norm identity is not asserted as new. Alexander, Fradelizi, García-Lirola and Zvavitch (2019/2020, §5.2) describe the complete-graph Lipschitz and free-space polytopes and determine their volume product. Their published formulas do not state an optimal Euclidean Banach--Mazur comparison in every dimension. The present statement adds the optimization over **all** Hilbertian norms, with an exact parity-dependent value. Some low-dimensional special cases of the distance are independently known; no priority is asserted for those specializations.

## Limitations
The conclusion is for finite *equilateral* metrics and real scalars. It does not determine distances for general graph metrics or complex Lipschitz-free spaces. Although the cited polytopal descriptions and elementary symmetry arguments make the conclusion accessible, equivalent formulas might occur under different names in older type-\(A\) root-polytope or oscillation-norm literature. Neither exhaustive bibliographic originality nor independent mathematical validation is claimed.

## References
1. A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178v1 (first public version 21 April 2009), §3, especially the discrete metric formula. https://arxiv.org/html/0904.3178v1
2. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v2 (2020), §§2 and 5.2, especially Claims 3–5. https://arxiv.org/html/1911.10642v2
