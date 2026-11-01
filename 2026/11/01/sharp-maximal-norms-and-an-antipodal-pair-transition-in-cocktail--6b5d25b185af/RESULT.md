# Sharp maximal norms and an antipodal-pair transition in cocktail-party graphs

## Finding
For each integer \(m\in\{2,3,4,5\}\), let \(G_m=K_{2,\ldots,2}\), the complete multipartite graph with \(m\) parts of size two. Equip it with unit graph distance and counting measure, and write \(M_m\) for the centered graph-ball Hardy--Littlewood maximal operator.

The sharp, attained strong real \(\ell^2\) constants and all extremizers are:

| \(m\) | \(\|M_m\|_{2\to2}^{\,2}\) | High antipodal pairs \(k_m\) | Common low/high ratio \(t_m\) | Labeled nonnegative extremal rays |
|---|---|---:|---|---:|
| \(2\) | \(\frac{7+2\sqrt{10}}9\) | 1 | \(\sqrt{10}-3\) | 2 |
| \(3\) | \(\frac{21+6\sqrt6}{25}\) | 1 | \(\frac{\sqrt6-2}{2}\) | 3 |
| \(4\) | \(\frac{43+4\sqrt{39}}{49}\) | 1 | \(\frac{2\sqrt{39}-9}{15}\) | 4 |
| \(5\) | \(\frac{65+10\sqrt{22}}{81}\) | 2 | \(\frac{\sqrt{22}-4}{3}\) | 10 |

Precisely, for any \(m\) in this range, choose any \(k_m\) of the \(m\) parts and set \(|f|=1\) at the \(2k_m\) vertices in those parts and \(|f|=t_m\) elsewhere. All nonzero extremizers, and no others, arise by positive scaling and independently changing vertex signs. The first change from one high pair to two high pairs occurs between \(m=4\) and \(m=5\), despite the unchanged radius-zero/radius-one/radius-two averaging structure. The new substantive instances are \(m=4,5\); the smaller instances are included to make the first-transition assertion exact.

## Assumptions and scope
Index the \(n=2m\) vertices by \(0,\ldots,n-1\) and pair vertex \(i\) with \(i\oplus1\), where \(\oplus\) denotes bitwise exclusive OR on the final bit. All distinct vertices are adjacent except paired vertices. Thus graph balls centered at \(i\) are exactly \(\{i\}\), \(V\setminus\{i\oplus1\}\), and \(V\). For any real vertex function \(f\), \(M_m f(i)\) is the maximum of the averages of \(|f|\) over these three balls. The norm is the unweighted \(\ell^2\) operator norm of this nonlinear map, \(\sup_{f\ne0}\|M_mf\|_2/\|f\|_2\).

No assertion is made for larger \(m\), weighted vertices, uncentered balls, or \(\ell^p\) with \(p\ne2\).

## Proof
**1. Exact finite reduction.** Write \(a_i=|f(i)|\) and \(S=\sum_i a_i\). The three admissible averages at vertex \(i\) are
\[
 a_i,\qquad \frac{S-a_{i\oplus1}}{n-1},\qquad\frac Sn.
\]
For every radius-selection vector \(z\in\{0,1,2\}^{n}\), let \(A_z\) have at row \(i\) the corresponding averaging vector. Because rows can be selected independently,
\[
 \|M_ma\|_2^2=\max_z\|A_za\|_2^2.
\]
Every \(A_z\) is nonnegative, and replacing an input by its absolute values cannot decrease \(\|A_zf\|_2\); hence the largest singular value is attained on a nonnegative input. Taking maxima gives
\[
 \|M_m\|_{2\to2}^2=\max_{z\in\{0,1,2\}^n}\lambda_{\max}(A_z^{\mathsf T}A_z).
\]
This is an exact identity, not a discretization of the input sphere.

**2. Integer separation of every competing selection.** Put \(L=\operatorname{lcm}(n,n-1)\), and write \(H_z=L A_z\); its rows are integer vectors. The following thresholds \(V_m/L^2\) are strictly below the corresponding claimed squared norm:

| \(m\) | \(n\) | \(L\) | \(V_m\) | \(T_m=V_m/L^2\) | Nonexceptional selections | Exceptional selections |
|---|---:|---:|---:|---|---:|---:|
| \(2\) | 4 | 12 | 210 | \(35/24\) | 79 | 2 |
| \(3\) | 6 | 30 | 1275 | \(17/12\) | 726 | 3 |
| \(4\) | 8 | 56 | 4350 | \(2175/1568\) | 6557 | 4 |
| \(5\) | 10 | 90 | 11178 | \(69/50\) | 59039 | 10 |

The exceptional selections are exactly those having radius zero at both vertices in each of \(k_m\) chosen antipodal parts and radius one everywhere else, where \((k_2,k_3,k_4,k_5)=(1,1,1,2)\). The companion program `verify.py` exhausts all \(3^n\) selections for each listed \(m\). For every nonexceptional selection it constructs an **integer** vector \(v\) with positive entries and checks, using unbounded exact integer arithmetic,
\[
 (V_m I-H_z^{\mathsf T}H_z)v>0
\]
entrywise. A numerical linear solve only proposes \(v\); the truth of the displayed strict integer inequalities, rechecked from the integer matrix, is the certificate. As \(H_z^{\mathsf T}H_z\) is a nonnegative matrix, its spectral radius is strictly below \(V_m\) by the positive-supervector comparison inequality. Thus all nonexceptional choices have squared operator norm strictly smaller than \(T_m\). The verifier reports 66,401 strict exclusions and 19 exceptional selections among 66,420 total choices.

**3. Algebraic evaluation of all exceptional choices.** Write \(q=2k_m\) and \(r=n-q\). After reordering pairs, every exceptional selection has the block form
\[
 A=\begin{pmatrix}I_q&0\\J_{r,q}/(n-1)&(J_r-P_r)/(n-1)\end{pmatrix},
\]
where \(J\) is an all-ones matrix and \(P_r\) interchanges the two vertices of each remaining pair. The input space decomposes orthogonally into the constants on the high and low blocks, the \((q-1)\)-dimensional zero-sum space on the high block, and the \((r-1)\)-dimensional zero-sum space on the low block. Under \(A^{\mathsf T}A\), the latter two spaces have eigenvalues \(1\) and \(1/(n-1)^2\), respectively. On the two constant-block directions, the singular-value matrix is
\[
 C=\begin{pmatrix}1&0\\\sqrt{qr}/(n-1)&(r-1)/(n-1)\end{pmatrix}.
\]
The larger eigenvalue of \(C^{\mathsf T}C\) is simple, positive, and greater than one. It is the larger root of
\[
 (n-1)^2\lambda^2-\bigl((n-1)^2+qr+(r-1)^2\bigr)\lambda+(r-1)^2=0.
\]
For the four cases the quadratic coefficient triples are \((9,-14,1)\), \((25,-42,9)\), \((49,-86,25)\), and \((81,-130,25)\), respectively. Their larger roots simplify to the four values in the Finding table. Substituting each rational \(T_m\) in the corresponding quadratic gives, respectively,
\[
-\frac{53}{192},\quad-\frac{47}{144},\quad-\frac{575}{50176},\quad-\frac{359}{2500}.
\]
All are negative, proving that the exceptional larger root strictly exceeds the separating threshold.

**4. Attainment and equality classification.** Let the candidate right singular vector equal \(1\) on the \(q\) high vertices and \(t\) on the remaining \(r\) vertices. Solving its eigenvector equations gives
\[
 t=\frac{(n-1)^2(\lambda-1)/r-q}{r-1},
\]
which simplifies to the four values in the Finding table. Direct radical inequalities show \(0<t<1\). With \(S=q+rt\), the high rows strictly select radius zero, since \(1>(S-1)/(n-1)\) and \(1>S/n\). The low rows strictly select radius one, since \((q+(r-1)t)/(n-1)>t\) and the excluded opposite vertex has value \(t<S/n\), making the radius-one average exceed the full average. Thus \(M_ma=A_za\) on the claimed positive singular vector, so the upper bound is attained.

Conversely, any nonzero equality case selects a matrix having the global top singular value; the strict certificate excludes all nonexceptional matrices. The larger eigenvalue for each exceptional matrix is simple because it exceeds one, so the nonnegative absolute-value profile must equal its unique positive top eigenvector up to scale. Radius choices are strict there. Every choice of \(k_m\) antipodal pairs yields one labeled nonnegative ray, giving \(\binom{m}{k_m}=2,3,4,10\); arbitrary independent signs produce exactly the real equality cases.

## Verification
Run `python verify.py` with Python 3 and NumPy installed; the program has no input data. It constructs the averaging matrices directly from the defining balls. A run returned:

```text
EXACT_CERTIFICATE m=2 selections=81 strict=79 exceptional=2
EXACT_CERTIFICATE m=3 selections=729 strict=726 exceptional=3
EXACT_CERTIFICATE m=4 selections=6561 strict=6557 exceptional=4
EXACT_CERTIFICATE m=5 selections=59049 strict=59039 exceptional=10
CERTIFICATE_OK selections=66420 strict=66401 exceptional=19
```

The full executable output additionally reports integer quadratic coefficients, rational separation thresholds and minimum strict integer margins. Numerical proposals for certificates are checked entirely by integer inequalities; no floating-point eigenvalue comparison is used as evidence. The program checks a finite exhaustive range, while the algebraic argument establishes exact constants and all equality cases for that range only.

## Relationship to prior work
Soria and Tradacete [1] introduce finite-graph maximal averaging and calculate sharp estimates for \(0<p\le1\), especially on complete graphs and stars. González-Riquelme and Madrid [2] establish sharp strong \(\ell^2\) norms for complete graphs and stars, not for complete multipartite cocktail-party graphs. González-Riquelme, Kovač and Madrid [3] study sharp graph *variation* constants and a five-vertex census, a different norm and smaller graph sizes. The exact \(m=3\) octahedral case was previously recorded and is included here as a comparison, not presented as new. The new conclusions are the exact \(m=4,5\) norms and the first change in heavy antipodal-pair count from one to two.

Searches for the graph aliases “cocktail-party”, “hyperoctahedral”, “Roberts”, “16-cell”, “complete multipartite with all parts two” and matching-deleted complete graphs found no source covering these exact \(\ell^2\) statements or their extremizer classification. A failed search is not a proof of absolute novelty; an unindexed calculation remains possible.

## Limitations
The theorem is finite in the graph-family parameter: no claim is made for \(m\ge6\), and the pattern in the table is not assumed to continue. The reported exhaustiveness is over the 66,420 **finite** averaging-radius choices in the stated four cases; it does not represent evidence for a conjecture about all cocktail-party graphs. The proof depends on the exact unit-edge metric and counting measure. Independent scientific validation and exhaustive publication-priority verification have not been performed.

## References
[1] J. Soria and P. Tradacete, “Best constants for the Hardy–Littlewood maximal operator on finite graphs,” arXiv:1410.6204, first public 2014-10-22, https://arxiv.org/abs/1410.6204.

[2] C. González-Riquelme and J. Madrid, “Sharp Inequalities for maximal operators on finite graphs,” arXiv:2005.03146, https://arxiv.org/abs/2005.03146.

[3] C. González-Riquelme, V. Kovač and J. Madrid, “Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs,” arXiv:2603.12462, https://arxiv.org/abs/2603.12462.
