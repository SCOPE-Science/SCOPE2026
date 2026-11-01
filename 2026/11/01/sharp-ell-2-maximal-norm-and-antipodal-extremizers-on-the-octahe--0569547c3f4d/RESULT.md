# Sharp \(\ell^2\) maximal norm and antipodal extremizers on the octahedral graph

## Finding

Let \(G\) be the one-skeleton of a regular octahedron, with its unweighted shortest-path metric, so \(G\cong K_{2,2,2}\). Its centered Hardy--Littlewood graph-ball maximal operator \(M\), with counting measure and real inputs, satisfies the exact, attained strong-type formula

\[
\boxed{\|M\|_{\ell^2(G)\to\ell^2(G)}=\sqrt{\frac{21+6\sqrt6}{25}}=1.194938298937632\ldots.}
\]

Every nonzero extremizer, and only such an extremizer, has absolute values of the form

\[
|f(v)|=\begin{cases}
a,&v\in\{u,\bar u\},\\
a(\sqrt6-2)/2,&v\notin\{u,\bar u\},
\end{cases}\qquad a>0,
\]

where \(\{u,\bar u\}\) is any of the three opposite, nonadjacent vertex pairs. Each coordinate sign can be chosen independently. Thus exactly three labeled nonnegative extremizing rays occur. The norm exceeds \(\sqrt{4/3}\), the previously established sharp norm for the complete graph \(K_6\), despite \(G\) being obtained from \(K_6\) by deleting a perfect matching [2].

## Assumptions and scope

The vertex set is \(V=\{0,1,2,3,4,5\}\), with nonedges exactly \(\{0,1\},\{2,3\},\{4,5\}\). Put \(\bar v=v\mathbin{\mathrm{xor}}1\), the unique nonneighbor of \(v\) other than itself. Edges have unit graph length and each vertex has counting mass one. For \(f:V\to\mathbb R\), define

\[
Mf(v)=\max_{r=0,1,2}\frac{1}{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|,
\quad \|f\|_2^2=\sum_{v\in V}|f(v)|^2.
\]

The only distinct balls at \(v\) are \(B(v,0)=\{v\}\), \(B(v,1)=V\setminus\{\bar v\}\), and \(B(v,2)=V\), of cardinalities \(1,5,6\). The statement concerns this finite, centered, counting-measure operator and unrestricted real inputs. No limit in graph size or other exponent is claimed.

## Proof

**Reduction to 729 linear matrices.** For a radius-choice vector \(s\in\{0,1,2\}^6\), let \(A_s\) be the nonnegative matrix whose row at \(v\) averages over \(B(v,s_v)\). The maximum in each output coordinate is independent, so for \(g=|f|\) we have exactly

\[
\|Mg\|_2^2=\max_{s\in\{0,1,2\}^6}\|A_sg\|_2^2.
\]

Every \(A_s\) has nonnegative entries, hence \(\|A_sx\|_2\le\|A_s|x|\|_2\) for every real \(x\). Therefore

\[
\|M\|_{2\to2}^2=\max_{s\in\{0,1,2\}^6}\lambda_{\max}(A_s^{\mathsf T}A_s).
\]

**Exact upper certificate outside three selections.** Put \(B_s=30A_s\). Its row at \(v\) is, according as \(s_v=0,1,2\), respectively \(30e_v^{\mathsf T}\), \(6(\mathbf1-e_{\bar v})^{\mathsf T}\), or \(5\mathbf1^{\mathsf T}\). For all choices except the following three,

\[
s_v=\begin{cases}0,&v\in\{2j,2j+1\},\\1,&\text{otherwise},\end{cases}
\qquad j\in\{0,1,2\},
\]

all six leading principal determinants of the integer symmetric matrix

\[
H_s=1269I_6-B_s^{\mathsf T}B_s
\]

are strictly positive. The embedded certificate program `octave_certificate.py` constructs all \(3^6=729\) choices and verifies every integer determinant using fraction-free Bareiss elimination, without floating-point decisions. It verifies precisely 726 strict cases and precisely the three exceptional cases above. By Sylvester's criterion, in each strict case \(H_s\) is positive definite, so

\[
\lambda_{\max}(A_s^{\mathsf T}A_s)<\frac{1269}{900}=\frac{141}{100}.
\]

**Analysis of the three exceptions.** Permuting the antipodal pairs reduces them to the choice with radius zero at vertices \(0,1\) and radius one elsewhere. Let \(R\) interchange vertices within each of the two remaining pairs, and let \(J_4\) be the four-by-four all-one matrix. Then, relative to the high pair and the other four vertices,

\[
A=\begin{pmatrix}I_2&0\\\frac15\mathbf1_{4\times2}&\frac15(J_4-R)\end{pmatrix}.
\]

The normalized indicator vectors of the high pair and of the other four vertices span an invariant two-dimensional subspace on which \(A\) acts as

\[
T=\begin{pmatrix}1&0\\\sqrt8/5&3/5\end{pmatrix}.
\]

Its Gram matrix has trace \(42/25\) and determinant \(9/25\). Hence its squared singular values are \((21\pm6\sqrt6)/25\). The orthogonal high-pair antisymmetric line has singular value one. On the three-dimensional low-vertex zero-sum subspace the restriction is \(-R/5\), with singular values \(1/5\). Therefore the exceptional top squared singular value is simple and equals

\[
\Lambda=\frac{21+6\sqrt6}{25}>\frac{141}{100};
\]

this dominates all other radius selections. The comparison follows from \(\sqrt6>19/8\).

**Attainment and exhaustive equality cases.** Put \(b=(\sqrt6-2)/2\), so \(0<b<1\), and let \(g=(1,1,b,b,b,b)\). At the first pair, radius zero gives \(1\), strictly exceeding both other ball averages. At each other vertex, radius one gives \((2+3b)/5\), strictly exceeding its own value \(b\) and the global average \((2+4b)/6\): the latter difference is \((1-b)/15>0\). Thus \(Mg=Ag\). Direct substitution into \(A^{\mathsf T}Ag=\Lambda g\) proves sharpness. Equality for any input forces a maximizing radius selection with squared norm \(\Lambda\); the strict 726-case certificate restricts this to the three exceptions. Each exceptional top singular eigenspace is one-dimensional and generated by the displayed strictly positive vector. All real inputs with those absolute values attain the norm, proving the classification.

## Verification

The standalone Python 3 verifier `octave_certificate.py` uses only standard-library integer and rational arithmetic for its finite exhaustive step. Run `python3 octave_certificate.py`. It checks all 729 radius selections; 726 have six strictly positive integer leading principal determinants for \(1269I_6-(30A_s)^{\mathsf T}(30A_s)\), and the remaining three are exactly the claimed exceptional selections. It also checks the exceptional eigenvector equations over \(\mathbb Q(\sqrt6)\). The expected successful terminal statement is `CERTIFICATE_OK all=729 strict=726 exceptional=3 witness=exact`.

These finite computations are exhaustive only because the operator has precisely three available radii at each of six vertices; the link from this finite certificate to the unrestricted real-input supremum is the analytical reduction in the first proof paragraph. The block decomposition and verification of active radii supply the mathematical equality argument.

## Relationship to prior work

Soria and Tradacete [1] introduced a systematic sharp-constant theory for centered graph-ball maximal operators, obtaining general results mainly for \(0<p\le1\) and examples including the four-cycle. González-Riquelme and Madrid [2] determined sharp strong \(\ell^2\) norms for complete graphs and stars, including \(\|M_{K_6}\|_2=\sqrt{4/3}\). Their continuation [3] treats the same classical families and other exponents and variation questions. The octahedral graph is neither complete nor a star nor a cycle: its radius-one ball omits precisely one antipodal vertex. The cited statements and inspected primary sections do not imply the present exact constant or extremizer classification. Targeted searches did not locate an earlier matching computation; this is not a proof of publication priority.

## Limitations

The result is restricted to the unweighted octahedral graph, counting measure, centered graph-distance balls, and the strong real \(\ell^2\) norm. It does not establish exact norms for larger cocktail-party graphs, weighted vertices, uncentered averages, or other exponents. The finite certificate is exact but is not a classification of all graphs. Possible unpublished or poorly indexed equivalent calculations remain a priority risk. Independent scientific validation has not been performed.

## References

[1] Javier Soria and Pedro Tradacete, *Best constants for the Hardy--Littlewood maximal operator on finite graphs*, arXiv:1410.6204, first posted 22 October 2014, https://arxiv.org/abs/1410.6204.

[2] Cristian González-Riquelme and José Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146, first posted 6 May 2020, https://arxiv.org/abs/2005.03146.

[3] Cristian González-Riquelme and José Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630, first posted 5 November 2020, https://arxiv.org/abs/2011.02630.
