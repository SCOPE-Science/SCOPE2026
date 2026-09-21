# Odd cycles identify symmetric measurement-error laws from sparse pairwise differences

## Setting

Let \(G=(V,E)\) be a simple comparison graph on \(V=\{1,\ldots,m\}\). A common latent quantity \(X\) is measured by
\[
Y_i=X+\varepsilon_i,
\]
where \(X,\varepsilon_1,\ldots,\varepsilon_m\) are mutually independent. For each comparison edge \(ij\in E\), suppose the marginal law of the collocated difference
\[
D_{ij}=Y_i-Y_j=\varepsilon_i-\varepsilon_j
\]
is known. Assume each error \(\varepsilon_i\) is centrally symmetric about zero and has a nowhere-zero characteristic function \(\varphi_i(t)\).

The question is whether sparse pairwise-difference laws determine the individual error laws, not merely their variances.

## Main theorem: an exact graph criterion

**Theorem.** The collection of error distributions \(\{\mathcal L(\varepsilon_i):i\in V\}\) is identified from \(\{\mathcal L(D_{ij}):ij\in E\}\) if and only if every connected component of \(G\) is non-bipartite, equivalently every connected component contains an odd cycle.

If this condition holds and the marginal law of one absolute measurement \(Y_r\) is also known, then the latent distribution \(\mathcal L(X)\) is identified as well.

The same statement holds for centrally symmetric \(\mathbb R^d\)-valued errors, with characteristic functions evaluated at \(t\in\mathbb R^d\).

### Proof

Central symmetry makes \(\varphi_i(t)\) real and even. Since \(\varphi_i(0)=1\), continuity together with the nowhere-zero assumption implies
\[
\varphi_i(t)>0\quad\text{for every }t.
\]
For an edge \(ij\), independence and symmetry give
\[
\Psi_{ij}(t):=\varphi_{D_{ij}}(t)
=\varphi_i(t)\varphi_j(-t)
=\varphi_i(t)\varphi_j(t)>0.
\]
Hence the real logarithms
\[
a_i(t)=\log\varphi_i(t),\qquad b_{ij}(t)=\log\Psi_{ij}(t)
\]
satisfy the linear system
\[
a_i(t)+a_j(t)=b_{ij}(t),\qquad ij\in E. \tag{1}
\]

The nullspace of the edge-by-vertex unsigned incidence matrix in (1) consists of vectors \(z\) satisfying \(z_i+z_j=0\) on every edge. On a connected component, values therefore alternate sign along every path. If the component is bipartite with parts \(A,B\), the assignment \(z=c\) on \(A\), \(z=-c\) on \(B\) gives a one-dimensional nullspace. If the component contains an odd cycle, alternating signs around that cycle force \(c=-c\), hence \(c=0\), and connectivity forces all coordinates to vanish. Thus (1) has a unique solution for all vertices exactly when every component is non-bipartite.

Solving (1) pointwise identifies every \(\varphi_i\), and uniqueness of characteristic functions identifies every error distribution.

Once \(\varphi_r\) is known, one absolute marginal gives
\[
\varphi_X(t)=\frac{\varphi_{Y_r}(t)}{\varphi_r(t)},
\]
which is well-defined because \(\varphi_r\) never vanishes. Thus \(\mathcal L(X)\) is identified.

## Constructive odd-cycle reconstruction

For an odd cycle
\[
v_0v_1,\ v_1v_2,\ldots,\ v_{2q}v_0,
\]
write \(b_k(t)=\log\Psi_{v_kv_{k+1}}(t)\), with indices modulo \(2q+1\). Then
\[
2a_{v_0}(t)=b_0(t)-b_1(t)+b_2(t)-\cdots+b_{2q}(t). \tag{2}
\]
After recovering \(a_{v_0}\), every adjacent vertex follows recursively from \(a_j=b_{ij}-a_i\). Thus one odd cycle anchors the component and tree branches can be propagated outward.

For three instruments this becomes the distributional three-cornered-hat identity
\[
\boxed{
\varphi_1(t)=
\sqrt{\frac{\Psi_{12}(t)\Psi_{13}(t)}{\Psi_{23}(t)}}
}
\]
and cyclic permutations, with the positive square root forced by the assumptions. Expanding log characteristic functions at the origin recovers the classical three-cornered-hat variance equations as the second-order special case.

## Sharp failure on bipartite comparison layouts

The graph condition is not merely an artifact of the logarithmic proof. Failure is already exact inside the Gaussian subclass.

Take one bipartite connected component with parts \(A,B\), independent errors
\[
\varepsilon_i\sim N(0,v_i),\qquad v_i>0.
\]
For sufficiently small nonzero \(c\), define
\[
v_i'=v_i+c\quad(i\in A),\qquad
v_j'=v_j-c\quad(j\in B).
\]
Every comparison edge crosses the bipartition, so
\[
v_i'+v_j'=v_i+v_j.
\]
Consequently every observed edge difference has exactly the same Gaussian law under \(v\) and \(v'\), even though the individual error laws differ.

This ambiguity survives observation of one absolute marginal. If the observed \(Y_r\) lies in the perturbed component and \(X\sim N(0,\tau^2)\), set
\[
\tau'^2=\tau^2-c\quad\text{when }r\in A,
\]
or \(\tau'^2=\tau^2+c\) when \(r\in B\). For sufficiently small \(|c|\), all variances remain positive and \(\tau'^2+v_r'=\tau^2+v_r\), so the absolute marginal is also unchanged. If \(r\) lies outside the perturbed component, no change to \(X\) is needed.

Thus a bipartite component gives genuine nonidentifiability within smooth, light-tailed, centrally symmetric models with nowhere-zero characteristic functions.

## Minimal sparse design

For \(m\ge3\), exactly \(m\) comparison edges are necessary and sufficient to identify all \(m\) error laws in this model class.

Necessity follows componentwise: a connected non-bipartite graph on \(k\) vertices must contain a cycle, hence has at least \(k\) edges. Summing over components gives \(|E|\ge m\).

Sufficiency is attained with exactly \(m\) edges: use a triangle and attach each of the remaining \(m-3\) vertices by one tree edge to any already connected vertex. The graph stays connected and contains an odd cycle. Therefore a spanning tree is never sufficient, but adding one edge that creates an odd cycle is enough.

## Relation to prior work

Three-cornered-hat methods classically recover individual error or oscillator variances from pairwise difference variances under independence. Gray and Allan (1974) explicitly derive the three variance equations and their solution for oscillator stability; modern reviews continue to formulate the method at the level of error variances. The graph-rank fact for unsigned incidence matrices is also standard and is not claimed as new.

Kotlarski-type repeated-measurement results identify latent and error distributions from the *joint distribution* of repeated measurements, a richer observation regime than the marginal laws of selected pairwise differences considered here. Nearing et al. (2017) developed a different nonparametric triple-collocation framework based on information quantities and emphasized underdetermination in a much more general observation model. Spicker (2024) uses symmetric replicate errors to construct empirical contrast-error distributions for nonparametric SIMEX, but does not provide the individual heterogeneous-error reconstruction or sparse comparison-graph criterion above. Ellis (2002) shows that a single convolution with an unknown symmetric factor is generally nonunique, illustrating why multiple linked convolutions supply essential additional structure.

To the best of our knowledge, the combination of (i) full error-distribution identification from pairwise-difference marginals, (ii) the exact odd-cycle criterion for arbitrary sparse comparison graphs, (iii) the sharp Gaussian bipartite alias, and (iv) the exact \(m\)-edge minimal design has not been stated in this form.

## Limitations

The result is a population-level identification theorem. It assumes additive collocated measurements of the same latent quantity, mutually independent errors, central symmetry about a known zero center, and nowhere-zero error characteristic functions. The logarithmic inversion can be numerically ill-conditioned when characteristic functions become small, so identification does not by itself imply stable finite-sample estimation.

Without symmetry, edge differences have characteristic functions \(\varphi_i(t)\overline{\varphi_j(t)}\), leaving phase ambiguities that the present theorem does not resolve. Characteristic-function zeros also require separate analysis. Correlated errors, nonadditive observation operators, noncollocated latent quantities, and inference from estimated rather than population difference laws are outside the claim.

## Reproducibility

`artifacts/verify.py` uses exact rational arithmetic and exhaustive simple-graph enumeration through six vertices. It verifies the unsigned-incidence rank criterion on every connected graph in that range, checks the minimal edge count for connected non-bipartite graphs, verifies the triangle product reconstruction with Laplace characteristic functions at a rational frequency, and checks an exact Gaussian bipartite alias including preservation of one absolute measurement variance. The recorded output is in `artifacts/VERIFICATION.txt`.

## References

- Grubbs, F. E. (1948). *On Estimating Precision of Measuring Instruments and Product Variability*. Journal of the American Statistical Association 43, 243–264. https://doi.org/10.1080/01621459.1948.10483261
- Gray, J. E. and Allan, D. W. (1974). *A Method for Estimating the Frequency Stability of an Individual Oscillator*. 28th Annual Symposium on Frequency Control, 243–246. https://doi.org/10.1109/FREQ.1974.200027 ; https://tf.nist.gov/general/pdf/57.pdf
- Sjoberg, J. P., Anthes, R. A., and Rieckh, T. (2021). *The Three-Cornered Hat Method for Estimating Error Variances of Three or More Atmospheric Datasets. Part I: Overview and Evaluation*. Journal of Atmospheric and Oceanic Technology 38. https://doi.org/10.1175/JTECH-D-19-0217.1
- Nearing, G. S. et al. (2017). *Nonparametric triple collocation*. Water Resources Research 53, 5516–5530. https://doi.org/10.1002/2017WR020359
- Vogel, A. and Ménard, R. (2023). *How far can the statistical error estimation problem be closed by collocated data?* Nonlinear Processes in Geophysics 30, 375–394. https://doi.org/10.5194/npg-30-375-2023
- Ellis, S. P. (2002). *Blind deconvolution when noise is symmetric: Existence and examples of solutions*. Annals of the Institute of Statistical Mathematics 54, 758–767. https://doi.org/10.1023/A:1022459217720
- Spicker, I. (2024). *Nonparametric simulation extrapolation for measurement-error models*. Canadian Journal of Statistics. https://doi.org/10.1002/cjs.11777
- Kotlarski, I. I. (1967). *On characterizing the gamma and normal distribution*. Pacific Journal of Mathematics 20, 69–76. https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-20/issue-1/On-characterizing-the-gamma-and-the-normal-distribution/pjm/1102992112.full
