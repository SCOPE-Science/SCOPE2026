# Equality cases for the sharp binary entropic uncertainty principle

## Finding
Let \(d\ge 0\) and let \(f\colon\mathbb Z^d\to\mathbb C\) be supported in \(\{0,1}\}^d\) with \(\|f\|_{\ell^2}=1\). Write
\[
c=\frac1{\ln 2}-1.
\]
Then equality in the sharp binary Beckner--Hirschman inequality
\[
H_{\mathbb T^d}(|\widehat f|^2)+c\,H_{\mathbb Z^d}(|f|^2)\ge0
\]
holds if and only if \(f\) is a constant-modulus linear phase on a proper affine Boolean cube. Explicitly, there are \(m\ge0\), \(b,v_1,\ldots,v_m\in\mathbb Z^d\), \(\phi\in\mathbb R\), and \(\eta\in\mathbb R^d\) such that the \(v_j\) are linearly independent over \(\mathbb Z\), every vertex
\[
A=b+\Big\{\textstyle\sum_{j=1}^m}\varepsilon_jv_j:\varepsilon_j\in\{0,1}\Big\}
\]
lies in \(\{0,1}\}^d\), and
\[
f(x)=2^{-m/2}e^{i\phi}e^{2\pi i\eta\cdot x}\mathbf 1_A(x).
\]
In particular, every equality state has support size \(2^m\) and has constant modulus \(2^{-m/2}\) on its support.

## Assumptions and scope
The torus carries normalized Haar measure. Entropies are measured in bits:
\[
H_{\mathbb Z^d}(|f|^2)=-\sum_x|f(x)|^2\log_2|f(x)|^2,
\qquad
H_{\mathbb T^d}(|\widehat f|^2)=-\int_{\mathbb T^d}|\widehat f(\xi)|^2\log_2|\widehat f(\xi)|^2\,d\xi,
\]
with \(0\log 0=0\). Fourier transform conventions agree with the cited binary-cube paper. A proper affine Boolean cube means the displayed subset-sum parametrization with integer-linearly independent generators; rank zero is a singleton.

The statement classifies equality for the Shannon-entropy limit of the sharp binary Hausdorff--Young inequality. It does not claim a quantitative stability estimate, nor does it classify equality for every Rényi parameter or for the separate convolution-entropy inequality.

## Proof
Define the entropy deficit
\[
\Delta_d(f)=H_{\mathbb T^d}(|\widehat f|^2)+c\,H_{\mathbb Z^d}(|f|^2).
\]
The cited 2025 paper proves \(\Delta_d(f)\ge0\). We identify the equality cases by a direct tensor decomposition.

First consider one dimension. For a normalized pair with squared moduli \(q\) and \(1-q\), the output density is, after a harmless translation of the torus variable,
\[
p_q(t)=1+2\sqrt{q(1-q)}\cos(2\pi t).
\]
Put \(\delta=|2q-1|\) and \(L=\ln2\). A direct Fourier-series computation gives
\[
K(\delta):=\int_0^1 p_q(t)\ln p_q(t)\,dt
=1-\delta+\ln\frac{1+\delta}2.
\]
Indeed, for \(0<\delta\le1\), set \(\rho=\sqrt{(1-\delta)/(1+\delta)}\). Then
\[
p_q(t)=\frac{|1+\rho e^{2\pi it}|^2}{1+\rho^2},
\]
and the Fourier series of \(\ln|1+\rho e^{2\pi it}|^2\) leaves only its first harmonic after multiplication by \(p_q\) and integration. The endpoint \(\delta=0\) follows by continuity.

Let
\[
h(\delta)=-\frac{1+\delta}2\ln\frac{1+\delta}2-\frac{1-\delta}2\ln\frac{1-\delta}2
\]
be the binary entropy in natural units, and define
\[
N(\delta)=-L K(\delta)+(1-L)h(\delta).
\]
The one-dimensional deficit equals \(N(\delta)/L^2\). Differentiation yields
\[
N'(\delta)=\frac{L\delta}{1+\delta}+\frac{1-L}2\ln\frac{1-\delta}{1+\delta},
\]
and
\[
N''(\delta)=\frac{2L-1-\delta}{(1-\delta)(1+\delta)^2}.
\]
Thus \(N'\) first increases and then decreases, because \(2L-1\in(0,1)\). Since \(N'(0)=0\), \(N'(\delta)\to-\infty\) as \(\delta\to1^-\), and \(N(0)=N(1)=0\), the function \(N\) is strictly positive on \((0,1)\). Consequently the one-dimensional entropy inequality has equality exactly when
\[
q\in\Big\{0,\frac12,1}\Big\}.
\]

Now split the last coordinate:
\[
f=(f_0,f_1),\qquad a_j=\|f_j\|_2^2,\qquad a_0+a_1=1.
\]
For every nonzero slice put \(g_j=f_j/\sqrt{a_j}\) and \(G_j=\widehat g_j\). For \(\xi\in\mathbb T^{d-1}\), set
\[
s(\xi)=a_0|G_0(\xi)|^2+a_1|G_1(\xi)|^2,
\qquad
u(\xi)=\frac{a_0|G_0(\xi)|^2}{s(\xi)}
\]
where \(s>0\). The Shannon chain rule for the discrete input, the corresponding mixture identity for the torus marginal \(s\), and the one-dimensional conditional Fourier inequality give the exact decomposition
\[
\Delta_d(f)=\sum_{j=0}^1 a_j\Delta_{d-1}(g_j)
+(1+c)\Big(h_2(a_0)-\int s(\xi)h_2(u(\xi))\,d\xi\Big)
+\int s(\xi)D_1(u(\xi))\,d\xi.
\]
Here \(h_2\) is binary entropy in bits and \(D_1\) is the nonnegative one-dimensional deficit just analyzed. The middle term is the mutual information between the slice label and the torus variable, hence is nonnegative. More explicitly it is a weighted Jensen--Shannon divergence, so it vanishes, when both slices are nonzero, exactly when
\[
|G_0(\xi)|^2=|G_1(\xi)|^2
\]
almost everywhere. Equality in the last term forces \(u(\xi)\in\{0,1/2,1}\) almost everywhere. If both slices are nonzero and the mutual-information term vanishes, then \(u\equiv a_0\), so equality forces \(a_0=a_1=1/2\).

We next use a rigidity fact for already classified lower-dimensional equality states. Suppose
\[
g(x)=2^{-m/2}e^{i\phi}e^{2\pi i\eta\cdot x}\mathbf 1_{b+\sum_j\{0,v_j\}}(x).
\]
Its autocorrelation
\[
C_g(z)=\sum_x g(x+z)\overline{g(x)}
\]
has the following exact form. If \(z=\sum_j\delta_jv_j\) with \(\delta_j\in\{-1,0,1}\), then uniqueness of the difference representation gives
\[
C_g(z)=2^{-|\{j:\delta_j\ne0\}|}e^{2\pi i\eta\cdot z};
\]
otherwise \(C_g(z)=0\). Hence the nonzero differences having largest modulus \(1/2\) are exactly \(\{\pm v_1,\ldots,\pm v_m}\), and the complex values there also recover the phase increments. Since \(|\widehat g|^2\) has Fourier coefficients \(C_g\), two phased affine-cube states with the same Fourier modulus are translates of one another up to a constant unimodular factor. The rank-zero case is immediate.

Induct on \(d\). If one slice vanishes, the lower-dimensional classification simply embeds into the corresponding last-coordinate hyperplane. If both slices are nonzero, equality in the decomposition above gives \(a_0=a_1=1/2\), both normalized slices are lower-dimensional equality states, and \(|G_0|=|G_1|\). By the rigidity fact,
\[
g_1(x)=\lambda g_0(x-t)
\]
for some \(t\in\mathbb Z^{d-1}\) and \(|\lambda|=1\). If the support of \(g_0\) has generators \(u_1,\ldots,u_m\), then the support of \(f\) is generated by
\[
(u_1,0),\ldots,(u_m,0),(t,1).
\]
The final generator is integer-linearly independent of the others because its last coordinate is one, and \(\lambda\) supplies its phase increment. Thus \(f\) has the asserted form.

Conversely, let \(f\) have the asserted form. Then
\[
\widehat f(\xi)=2^{-m/2}e^{i\phi}e^{-2\pi ib\cdot\xi}\prod_{j=1}^m\bigl(1+e^{2\pi i\eta\cdot v_j}e^{-2\pi iv_j\cdot\xi}\bigr).
\]
Because \(v_1,\ldots,v_m\) are integer-linearly independent, the homomorphism \(\mathbb T^d\to\mathbb T^m\) given by \(\xi\mapsto(v_1\cdot\xi,\ldots,v_m\cdot\xi)\) pushes Haar measure to Haar measure. Therefore the output entropy is the sum of \(m\) copies of the balanced one-dimensional output entropy, while the input entropy is \(m\). The one-dimensional equality already proved gives \(\Delta_d(f)=0\). This completes both directions.

## Verification
The proof is exact and dimension-free. The packaged script `verify_entropy_extremizers.py` independently checks the symbolic derivative identities for the strict one-dimensional deficit, compares the closed form against high-resolution numerical quadrature, tests positivity away from the three one-dimensional equality points, checks several multidimensional equality and nonequality examples, and verifies the autocorrelation signature that recovers the generator directions of a phased affine cube. The stored output ends with `VERIFY_OK`.

These computations are supplementary: positivity and the all-dimensional classification are proved analytically above rather than inferred from numerical sampling.

## Relationship to prior work
Crmarić, Kovač, and Shiraki proved the sharp binary entropic uncertainty inequality in 2025 as Corollary 5 of their binary-cube Fourier paper. Their statement records that equality is attained for the normalized constant function on the full binary cube, and Section 7 verifies that example. The inspected statement and proof do not classify all equality states.

The classification here extracts the equality conditions through a Shannon chain-rule decomposition rather than only differentiating the sharp Hausdorff--Young inequality. The new structural ingredient is the phased autocorrelation rigidity lemma, which upgrades equality of Fourier magnitudes for lower-dimensional extremizers to translation and constant-phase equivalence. The resulting family is substantially larger than the single displayed example: it includes singletons, diagonal and higher-rank affine Boolean cubes, arbitrary translations allowed by the ambient binary cube, and arbitrary linear modulations.

General compact/discrete abelian-group Fourier norm and Rényi-uncertainty results provide broader background, but they do not directly imply this support-refined binary coefficient or the phased affine-cube equality classification. The previous ordinary-additive-energy equality theorem for indicator sets also does not imply the present complex-valued entropy statement: it neither controls phases nor supplies the entropy chain-rule rigidity used here.

## Limitations
The originality assessment is literature-dependent. Targeted web and semantic-record searches did not locate an equivalent equality classification, but an unindexed note, folklore argument, or terminology mismatch remains possible. One broader compact/discrete abelian-group source was compared only at abstract level and is therefore not used to assert absence of a hidden equivalent theorem from its full text.

No quantitative stability estimate is proved. The theorem also does not classify equality for the full one-parameter family of sharp binary Hausdorff--Young inequalities or for the separate entropy-of-sums inequality.

## References
1. Tonći Crmarić, Vjekoslav Kovač, and Shobu Shiraki, *Inequalities in Fourier analysis on binary cubes*, arXiv:2507.01359, first posted 2025-07-02. Primary MSC 2020: 42A05. https://arxiv.org/abs/2507.01359
2. Mokshay Madiman and Peng Xu, *The norm of the Fourier transform on compact or discrete abelian groups*, Journal of Fourier Analysis and Applications 26 (2020), article 37. https://doi.org/10.1007/s00041-020-09737-7
