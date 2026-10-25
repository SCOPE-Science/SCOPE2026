# Spoke-pair resistance interactions on wheel networks

## Finding

For every integer \(n\ge3\), let \(W_n=K_1\vee C_n\) have unit conductances, a central hub, and rim vertices numbered cyclically. Write \(K(G)\) for the sum of effective electrical resistances over unordered vertex pairs. Delete one hub-to-rim spoke and denote its Kirchhoff-index increase by \(S_n\). Delete instead two distinct spokes at shorter cyclic separation \(1\le d\le m=\lfloor n/2\rfloor\), and denote the increase by \(D_n(d)\). All these deletion graphs are connected.

**Theorem.** For every \(n\ge4\), \(D_n(1)>D_n(d)\) for every \(2\le d\le m\). Thus the exactly \(n\) adjacent-spoke pairs are the unique maximum-damage spoke pairs (the statement is trivially true for \(n=3\)). The interaction \(I_n(d)=D_n(d)-2S_n\) has a *single separation sign transition*: it is positive at \(d=1\), and its sign can change from positive to negative at most once as \(d\) increases; a zero, if present, occurs at only one separation. For \(3\le n\le5\), it is positive at every permitted separation, whereas for every \(n\ge6\), \(I_n(m)<0\). In particular, the six-rim wheel is the first with a pair of spoke failures causing less aggregate resistance damage than twice an isolated failure. Define \(k_n=\min\{d:I_n(d)<0\}\) for \(n\ge6\). Then
\[
 k_n=\frac{\log n+\log\log n}{\log((3+\sqrt5)/2)}+O(1)\qquad(n\to\infty).
\]
The threshold is effectively exact at each finite \(n\) through the formulas below; no universal closed elementary formula for its integer value is claimed.

Set \(N=n+1\), \(r=(3-\sqrt5)/2\), and for \(0\le d\le m\) put
\[
 c_d=\frac{r^d+r^{n-d}}{\sqrt5(1-r^n)},\quad
 u_d=c_d\left[\frac35+
 \frac{d r^d+(n-d)r^{n-d}}{\sqrt5(r^d+r^{n-d})}
 +\frac{nr^n}{\sqrt5(1-r^n)}\right].
\]
Define \(\alpha=1-c_0\) and \(\sigma=u_0-1/N\), both strictly positive. Then the **exact damage and interaction formulas** are
\[
 S_n=\frac{N\sigma}{\alpha},\qquad
 D_n(d)=\frac{2N[\alpha\sigma+c_d(u_d-1/N)]}{\alpha^2-c_d^2},
\]
\[
 I_n(d)=\frac{2Nc_dY_d}{\alpha(\alpha^2-c_d^2)},\qquad
 Y_d=\alpha\left(u_d-\frac1N\right)+\sigma c_d.
\]
Every denominator is positive. The sequence \(Y_1,\ldots,Y_m\) is strictly decreasing. Therefore the sign transition and \(k_n\) are determined exactly by evaluating the displayed elementary expressions, not by graph inversion.

## Assumptions and scope

Graphs are simple and undirected; all rim and spoke conductances equal one. Wheel notation uses \(n\) **rim** vertices and \(n+1\) total vertices. Only unordered pairs of distinct spoke failures are optimized; the theorem does not compare rim-edge failures, more than two failures, or weighted wheels. \(K(G)\) uses unordered vertex pairs, without degree normalization. Asymptotic \(O(1)\) is uniform in integer \(n\) and refers to the first *negative* interaction separation.

## Proof

**1. Grounded Green kernel.** Ground the hub of \(W_n\). Its rim Dirichlet Laplacian is the cyclic matrix \(A_n=3I-S-S^{-1}\), where \(S\) is cyclic translation. Write \(G=A_n^{-1}\) and \(H=A_n^{-2}\). The positive inverse has entries \(G_{0d}=c_d\) and \(H_{0d}=u_d\). One derivation uses the infinite-line kernels
\[
 g_j=\frac{r^{|j|}}{\sqrt5},\qquad
 h_j=r^{|j|}\left(\frac3{5\sqrt5}+\frac{|j|}{5}\right),
\]
which satisfy \((3I-S-S^{-1})g=\delta_0\) and \(h=g*g\). Periodizing each kernel modulo \(n\) gives \(c_d=\sum_{k\in\mathbb Z}g_{d+kn}\), \(u_d=\sum_{k\in\mathbb Z}h_{d+kn}\), and summing the geometric and differentiated-geometric series yields the displayed closed forms. The \(n\)-rim matrix has row sum one for its inverse, because \(A_n\mathbf1=\mathbf1\).

**2. Two-spoke deletion.** Orient each spoke from hub to its rim vertex, and let \(b_i\) be its incidence column. In the original wheel, the Gram matrix \(B^\mathsf TL^+B\) for the two selected spokes is
\(\begin{psmallmatrix}c_0&c_d\\c_d&c_0\end{psmallmatrix}\). The Gram matrix \(B^\mathsf T(L^+)^2B\) is
\(\begin{psmallmatrix}\sigma&u_d-1/N\\u_d-1/N&\sigma\end{psmallmatrix}\): the grounded response to one spoke is the corresponding column of \(G\), and subtracting its mean \(1/N\) produces the zero-mean pseudoinverse response. By the rank-two Woodbury identity on the zero-sum subspace,
\[
 (L-BB^\mathsf T)^+=L^++L^+B(I-B^\mathsf TL^+B)^{-1}B^\mathsf TL^+.
\]
Deleting any two spokes retains the rim cycle, hence the matrix \(I-B^\mathsf TL^+B\) is positive definite. In particular \(\alpha>c_d>0\). Since \(K(G)=N\operatorname{tr}L^+\), evaluating the trace gives \(D_n(d)\). The rank-one version gives \(S_n\); subtracting twice that expression gives \(I_n(d)\) and its controlling numerator \(Y_d\).

**3. Monotonic kernels and unique worst pair.** Both infinite sequences \(g_j\) and \(h_j\) for \(j\ge0\) are strictly decreasing and strictly discretely convex. For \(g\) this is immediate from \(0<r<1\). For \(h_j=r^j(A+Bj)\), \(A=3/(5\sqrt5)\) and \(B=1/5\), the decrease and convexity reduce respectively to
\[
 (1-r)A-rB=\frac{\sqrt5}{25}>0,
 \qquad (1-r)A-2rB=\frac{7\sqrt5-15}{50}>0.
\]
For either kernel \(f\), let \(\delta_j=f_j-f_{j+1}\); it is positive and strictly decreasing. Its periodization \(p_d=\sum_{k\in\mathbb Z}f_{|d+kn|}\) satisfies
\[
 p_d-p_{d+1}=\sum_{j\ge0}\bigl(\delta_{jn+d}-\delta_{(j+1)n-d-1}\bigr)>0
\]
whenever \(2d+1<n\). Therefore \(c_d\) and \(u_d\) strictly decrease over \(0\le d\le m\). Because \(\alpha,\sigma>0\), so does \(Y_d\). Once \(Y_d<0\), every later interaction is negative; before then there can be at most one zero. The adjacency interaction is positive by Step 4. On the nonnegative portion of \(Y_d\), \(c_dY_d/(\alpha^2-c_d^2)\) is strictly decreasing, and all negative interactions are smaller than \(I_n(1)>0\). Thus \(D_n(1)>D_n(d)\) for \(d>1\). Exactly \(n\) unordered spoke pairs are cyclically adjacent.

**4. Sharp onset of negative interaction.** For \(n\ge5\), the infinite-line convolution gives
\(u_1\ge h_1=2/(5\sqrt5)>1/6\ge1/N\); hence \(Y_1>0\). For \(n=3,4\) the same follows directly (\(u_1-1/N=1/16\) and \(1/25\), respectively). At maximum separation \(m\), exact calculations give
\[
 (Y_m)_{n=3,4,5,6,7}
 =\left(\frac1{16},\frac4{225},\frac1{726},-\frac{51}{2800},-\frac{165}{6728}\right).
\]
It remains to show \(Y_m<0\) for \(n\ge8\). From \(c_0=(1+r^n)/(\sqrt5(1-r^n))\le c_0|_{n=3}=1/2\) and \(H\preceq G\) (all eigenvalues of \(A_n\) are at least one), we obtain \(0<\sigma<\alpha\). Therefore \(Y_m/\alpha<u_m+c_m-1/N\). Set \(q=2/5\). For all \(j\ge0\),
\[
 h_j+g_j=r^j\left(\frac8{5\sqrt5}+\frac j5\right)
 <q^j\left(\frac45+\frac j5\right).
\]
The absolute distances \(|m+kn|\), \(k\in\mathbb Z\), occur in pairs whose \(j\)-th pair is at least \((2j+1)m\). With \(x=q^{2m}\), summing the majorant gives
\[
 (n+1)(u_m+c_m)
 \le (2m+2)\,2q^m\left[
 \frac{4/5+m/5}{1-x}+\frac{(2m/5)x}{(1-x)^2}
 \right]=B_m.
\]
For each fixed summand of the series defining \(B_m\), increasing \(m\ge4\) multiplies it by at most \(3/5\): bound the prefactor ratio by \(6/5\), the exponential ratio by \(2/5\), and the affine factor ratio by \(5/4\). Consequently \(B_m\) is strictly decreasing for \(m\ge4\), while the exact evaluation
\[
 B_4=\frac{125000000000}{152387956161}<1
\]
proves \((n+1)(u_m+c_m)<1\) for every \(n\ge8\). This implies \(Y_m<0\), completing the sharp \(n=6\) onset and all-sign classification.

**5. Asymptotic first-negative separation.** At \(d=O(\log n)\), the periodized kernels satisfy, uniformly,
\[
 \frac{Y_d}{\alpha}
 =r^d\left(\frac d5+O(1)\right)-\frac1{n+1}
 +O(nr^{n-d}).
\]
Here \(\alpha\) stays bounded away from zero and \(\sigma/\alpha\) is bounded. Since \(nr^{n-d}\) is negligible for such \(d\), evaluating this expression at integers within a fixed distance of \((\log n+\log\log n)/\log(1/r)\), choosing the fixed distance sufficiently large on each side, yields respectively positive and negative signs. Strict decrease of \(Y_d\) then traps the first negative separation \(k_n\) between these two choices. Since \(1/r=(3+\sqrt5)/2\), the asserted asymptotic follows.

## Verification

Run `python verify.py` with SymPy installed as specified in `requirements.txt`. It independently constructs exact wheel Laplacians for \(3\le n\le13\), inverts grounded rim matrices, and checks the two-spoke damage formula against direct zero-sum inverse traces for every allowed cyclic separation. It verifies the single-spoke formula, the exact radical Green-kernel expressions, the interaction identity, the five boundary signs, maximum-damage classification on those sizes, and the \(m=4\) exact majorant. The expected output is `VERIFY_OK 222 independent exact wheel damages, Green entries, pair identities, sign cases; bound`. These finite checks are diagnostic; Steps 1–5 prove the infinite-family result.

## Relationship to prior work

Carmona, Mitjana and Monsó (arXiv:1609.04642v1, first posted 13 September 2016) compute Green kernels and Kirchhoff indices of subdivision networks, with a detailed wheel example. Its wheel formulas provide close algebraic context but not the present optimization over a pair of removed spokes, the interaction-sign threshold, or its logarithmic-logarithmic onset. Gago's 2016 non-complete wheel work treats a hub connected to equally spaced cycle vertices, a structurally different subfamily; the complete text could not be retrieved, so specialized overlap remains a documented risk. The rank-two Laplacian update itself is standard and is not claimed as new. The result here is the sharp comparison and sign-transition theorem, not the Green matrix alone.

## Limitations

Only pairs of hub spokes are considered. The first-negative index is given by an exact finite test and its asymptotic scale, but no simpler uniform integer closed form is proved. The self-review correctness assessment is not an independent audit. Searches and text inspections cannot establish the absence of an equivalent result in all specialized literature; the inaccessible Gago paper is a particular residual risk. No experimental run establishes the infinite claim.

## References

1. Ángeles Carmona, Margarida Mitjana, Enric Monsó, *Effective resistances and Kirchhoff Index in subdivision networks*, arXiv:1609.04642v1, publicly posted 2016-09-13, https://arxiv.org/abs/1609.04642 .
2. Silvia Gago, *The group inverse of extended symmetric and periodic Jacobi matrices*, research report dated 2016-02-02, https://hdl.handle.net/2117/124693 .
3. Silvia Gago, *Kirchhoff index of a non-complete wheel*, Electronic Notes in Discrete Mathematics 54 (2016), 229–234, DOI:10.1016/j.endm.2016.09.040 .
4. Heping Zhang and collaborators, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107 (2007), 330–339, DOI:10.1002/qua.21068 .
