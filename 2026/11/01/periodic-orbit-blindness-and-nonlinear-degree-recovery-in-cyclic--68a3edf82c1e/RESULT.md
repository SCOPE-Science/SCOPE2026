# Periodic-orbit blindness and nonlinear degree recovery in cyclic Chebyshev maps

## Finding

For each integer \(b_1,b_2,b_3\geq2\), define the first-kind Chebyshev polynomial \(T_m\) by \(T_m(\cos\theta)=\cos(m\theta)\), and define the continuous self-map of \([-1,1]^3\)
\[
F(x_1,x_2,x_3)=\bigl(T_{b_1}(x_2),T_{b_2}(x_3),T_{b_3}(x_1)\bigr).
\]
Put \(B=b_1b_2b_3\). Then **every positive iterate has exactly**
\[
\#\operatorname{Fix}(F^n)=B^n\qquad(n\geq1).
\]
Consequently the Artin–Mazur zeta function and topological entropy are exactly
\[
\zeta_F(z)=\frac1{1-Bz},\qquad h_{\mathrm{top}}(F)=\log B.
\]
The unique measure of maximal entropy is \(\mu=\nu^{\otimes3}\), with \(d\nu(x)=dx/(\pi\sqrt{1-x^2})\). It does **not** depend on the three degrees. Moreover, \(F\) with this probability is measurably isomorphic to the uniform one-sided full shift on \(B\) symbols. Hence **two degree triples yield isomorphic maximal-entropy measure-preserving maps if and only if their products are equal**.

There is a complementary exact parameter-identification law. Let \(\pi(1)=2\), \(\pi(2)=3\), \(\pi(3)=1\); for \(i\in\{1,2,3\}\) and integers \(n\geq0\), put
\[
M_{i,n}=\prod_{r=0}^{n-1}b_{\pi^r(i)},\qquad M_{i,0}=1.
\]
For every \(i,j\in\{1,2,3\}\), \(k,\ell\geq1\) and \(n\geq0\), the stationary Chebyshev-mode correlation is
\[
\boxed{\int T_k\bigl((F^n(x))_i\bigr)T_\ell(x_j)\,d\mu(x)
 =\tfrac12\,\mathbf1_{\{j=\pi^n(i)\}}\,\mathbf1_{\{\ell=kM_{i,n}\}}.}
\]
In particular, all stationary raw-coordinate cross-covariances at every **positive** time lag are zero, although the system is deterministic. Yet the three degree labels are recovered separately and without ambiguity from the one-step nonlinear moments
\[
\boxed{\int (F(x))_i\,T_k(x_{\pi(i)})\,d\mu(x)
  =\begin{cases}\tfrac12,&k=b_i,\\0,&k\ne b_i,\end{cases}\qquad k\geq1.}
\]
Therefore the complete periodic-point counts, entropy and even the maximal-entropy measure-theoretic isomorphism class distinguish only the product \(B\); stationary one-time distributions and ordinary lagged coordinate covariances distinguish no degrees at all. Nevertheless, the displayed nonlinear moments recover the **ordered** triple \((b_1,b_2,b_3)\) when coordinate labels are retained.

## Assumptions and scope

All assertions concern the exact real map on the closed cube, **not** a finite-precision implementation. The degrees \(b_i\) are integers at least two. The motivating published construction allows real degree parameters in \((0,6)\); the present results apply to its natural polynomial subfamily \(b_i\in\{2,3,4,5\}\) and, mathematically, to all larger integer degrees. The measure \(\mu\) is the specified stationary maximal-entropy measure. The lag-correlation formulas are not assertions about arbitrary initial distributions or noninteger degree parameters.

## Proof

**1. Cyclic reduction.** Chebyshev composition obeys \(T_m\circ T_n=T_{mn}\) for positive integers, by substituting \(x=\cos\theta\). Thus, coordinatewise,
\[
(F^n(x))_i=T_{M_{i,n}}(x_{\pi^n(i)}),\qquad
F^3=(T_B,T_B,T_B).
\]
The product \(\prod_{i=1}^3M_{i,n}=B^n\), because each degree occurs exactly \(n\) times as \(i\) traverses the three coordinates. If \(3\mid n\), each \(M_{i,n}=B^{n/3}\).

**2. Exact scalar fixed-point count.** For every integer \(D\geq2\), \(T_D(x)=x\) on \([-1,1]\) has exactly \(D\) solutions. Indeed, setting \(x=\cos\theta\), with the *unique* \(\theta\in[0,\pi]\), the equation becomes \(\cos(D\theta)=\cos\theta\), equivalently \(\theta=2\pi r/(D-1)\) or \(\theta=2\pi s/(D+1)\) in \([0,\pi]\). For even \(D=2q\), the two sets have \(q\) and \(q+1\) members and intersect only at \(0\), yielding \(2q=D\). For odd \(D=2q+1\), their cardinalities are \(q+1\) and \(q+2\) and their only common angles are \(0\) and \(\pi\), again yielding \(2q+1=D\). This explicitly accounts for endpoint coincidences.

**3. Fixed points of all iterates.** For \(3\mid n\), the reduction in step 1 gives three independent scalar equations \(T_{B^{n/3}}(x_i)=x_i\), hence \((B^{n/3})^3=B^n\) solutions. Otherwise \(\pi^n\) is a three-cycle. The three fixed-point equations successively determine two coordinates uniquely from the third (without requiring any inverse of a Chebyshev polynomial). Substitution leaves \(T_{\prod_iM_{i,n}}(x_i)=x_i\), that is, \(T_{B^n}(x_i)=x_i\). Step 2 gives exactly \(B^n\) solutions, each extending to one and only one triple. The zeta identity follows from the formal exponential \(\exp(\sum_{n\geq1}B^nz^n/n)=(1-Bz)^{-1}\). The number of points of *least* period \(n\) is consequently \(\sum_{d\mid n}\mathrm{mob}(d)B^{n/d}\), with \(\mathrm{mob}\) the arithmetic Möbius function.

**4. Entropy, the stationary law and complete metric classification.** The homeomorphism \(h(u)=\cos(\pi u)\) sends \([0,1]\) to \([-1,1]\). Each \(g_m=h^{-1}\circ T_m\circ h\) is the continuous zigzag map with \(m\) equal-length full branches of slope \(\pm m\). Therefore \(G=h^{-1}\circ F\circ h\), applying \(h\) coordinatewise, has precisely \(B\) rectangular full branches onto \([0,1]^3\). Each inverse branch contracts the sup metric by at most \(1/2\), and each forward branch has constant absolute Jacobian \(B\). Thus normalized three-dimensional Lebesgue measure is invariant. The sequence of visited full-branch labels is independent and uniform on \(B\) symbols, because each branch has volume \(1/B\) and conditional output is again uniform; inverse-branch contraction makes this partition generating off a Lebesgue-null set of branch boundaries. This gives a measure-theoretic isomorphism with the uniform one-sided \(B\)-shift, not an everywhere topological conjugacy.

The same coding proves the maximal entropy is \(\log B\) and uniqueness of the maximal-entropy measure: any invariant measure with entropy rate \(\log B\) must have uniform iid labels for its full-branch generating partition; exceptional branch boundaries have entropy zero and cannot support a maximal-entropy measure. In original coordinates the pushforward of Lebesgue is \(\mu=\nu^{\otimes3}\), with \(d\nu(x)=dx/(\pi\sqrt{1-x^2})\). This also agrees with the alternative identity \(F^3=(T_B,T_B,T_B)\) and \(h_{\mathrm{top}}(F^3)=3h_{\mathrm{top}}(F)\). Two such systems with the maximal-entropy measures are isomorphic if the degree products agree, by the full-shift codings; the converse follows from equality of entropy under measure-theoretic isomorphism.

**5. Complete mode correlations and degree recovery.** Chebyshev orthogonality under \(\nu\) gives, for positive integers \(r,s\),
\[
\int T_r\,d\nu=0,\qquad\int T_rT_s\,d\nu=\tfrac12\,\mathbf1_{\{r=s\}}.
\]
The product measure has independent coordinates. By step 1 and \(T_k\circ T_M=T_{kM}\), the left observable in the stated mode-correlation integral depends only on input coordinate \(\pi^n(i)\), with degree \(kM_{i,n}\). Independence (if the input coordinates differ) and orthogonality (if they agree) give the displayed exact formula. For raw coordinates take \(k=\ell=1\); at every positive lag \(M_{i,n}\geq2\), so the correlation vanishes for all coordinate pairs, while all means are zero. Finally take \(n=1,k=1,j=\pi(i)\) and let \(\ell\) vary: a moment of \(1/2\) occurs at precisely \(\ell=b_i\), recovering every labeled degree.

## Verification

The self-contained `checks/verify.py` uses exact integers and rational arithmetic to check the scalar angle census for \(D=2,\ldots,500\), finite composition identities, the third-iterate reduction, cyclic multiplier identities for all \(64\) degree triples in \(\{2,3,4,5\}^3\) and time indices \(1,\ldots,12\), and indexing of nonlinear moments. It passes \(25\) symbolic Chebyshev-composition checks, \(499\) exact angle checks, \(768\) cyclic-multiplier checks and \(270\) correlation-indexing checks. These checks are **supporting finite experiments**, not substitutes for the all-degree and all-time arguments in the proof. Run with `python checks/verify.py`; the program requires Python 3 and SymPy.

## Relationship to prior work

Zhang, Xiang, Zhang and Liu defined the three-dimensional cyclic symmetric Chebyshev map and reported numerical dynamical statistics; the map itself is not claimed as new. Yan and Beck derived invariant densities and higher-order correlations for individual Chebyshev maps, and considered *diffusively* coupled maps; their one-dimensional zero two-point correlations are acknowledged. The algebraic relation \(T_m\circ T_n=T_{mn}\) and classical full-branch entropy theory are also standard. The specific contribution is the combined **complete maximal-entropy isomorphism classification, exact every-period census, and information-separation theorem** for this coordinate-permuting three-dimensional family: periodic and linear statistics conceal degree labels while an exact nonlinear one-step signature recovers them. A later image-encryption application of the same cyclic map does not establish this dynamical classification. No claim is made that single-map Chebyshev correlation vanishing, or the original cyclic construction, was first observed here.

## Limitations

The assertion is exact for integer degrees only; it does not settle noninteger Chebyshev parameters or floating-point arithmetic. The stationary measure is not a statement about every initial distribution. Parameter recovery requires labeled coordinate observations, an exact expectation and access to Chebyshev modes; this is not a cryptographic-security theorem. Prior publication of an equivalent unindexed calculation remains possible. Some publisher-hosted primary full text was not directly retrievable for inspection, so publication-priority assessment has a specific residual access limitation. No independent mathematical audit has been performed.

## References

1. Y. Zhang, H. Xiang, S. Zhang, L. Liu, *Construction of high-dimensional cyclic symmetric chaotic map with one-dimensional chaotic map and its security application*, *Multimedia Tools and Applications* (first public online 2022-10-12), DOI: 10.1007/s11042-022-14044-y; open-indexed text: https://pmc.ncbi.nlm.nih.gov/articles/PMC9554847/ .
2. J. Yan and C. Beck, *Distinguished correlation properties of Chebyshev dynamical systems and their generalisations*, arXiv:2006.06786 (2020), https://arxiv.org/html/2006.06786v1 .
3. T. Kohda, A. Tsuneda, A. J. Lawrance, *Correlational Properties of Chebyshev Chaotic Sequences*, *Journal of Time Series Analysis* 21 (2000), 181–191, DOI: 10.1111/1467-9892.00180.
4. A. Pakapongpun and T. Ward, *Orbits for products of maps*, *Thai Journal of Mathematics* 12 (2014), 33–44, https://eprints.whiterose.ac.uk/id/eprint/103802/ .
5. S. Kanwal et al., *An efficient image encryption algorithm using 3D-cyclic chebyshev map and elliptic curve*, *Scientific Reports* 14 (2024), 29626, DOI: 10.1038/s41598-024-77955-w.
