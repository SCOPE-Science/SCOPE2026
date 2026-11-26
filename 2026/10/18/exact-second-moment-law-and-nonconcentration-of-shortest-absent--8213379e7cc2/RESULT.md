# Exact second moments and relative variance of shortest absent binary subsequences

## Finding

Fix the alphabet \(\{0,1\}\), even when the source word uses only one letter. Let \(S(w)\) count the distinct binary words of minimum length that are not subsequences of \(w\). In particular, \(S(\varepsilon)=2\). Define
\[
A_{a,b}=\sum_{|w|_0=a,\,|w|_1=b}S(w),\qquad
B_{a,b}=\sum_{|w|_0=a,\,|w|_1=b}S(w)^2.
\]
The bivariate ordinary generating functions are
\[
\begin{aligned}
F_1(x,y)&=\sum_{a,b\ge0}A_{a,b}x^ay^b
=\frac{2-x-y}{1-x-y-2xy+2x^2y+2xy^2-x^2y^2},\\
F_2(x,y)&=\sum_{a,b\ge0}B_{a,b}x^ay^b
=\frac{4-3x-3y+2x^2y+2xy^2-2x^2y^2}
{1-x-y-4xy+4x^2y+4xy^2-x^2y^2-2x^3y^2-2x^2y^3+2x^3y^3}.
\end{aligned}
\]
If \(W_{n,k}\) is uniform on length-\(n\) binary words of weight \(k\), then
\[
\operatorname{Var}S(W_{n,k})=
\frac{B_{n-k,k}}{\binom nk}-\left(\frac{A_{n-k,k}}{\binom nk}\right)^2
\qquad (n\ge0,\ 0\le k\le n).
\]
At length \(10\) and weight \(5\), the mean is \(185/42\) and the variance is \(12331/588\).

Let \(W_n\) instead be uniform on all \(2^n\) binary sources, and define
\[
P_1(z)=1-z-3z^2+z^3,\qquad P_2(z)=1-z-5z^2+3z^3+2z^4-2z^5.
\]
Their unique smallest-modulus zeros are simple, with \(r_1\in(0.460811,0.460812)\) and \(r_2\in(0.406865,0.406866)\), respectively. Then
\[
\mathbb ES(W_n)\sim C_1(2r_1)^{-n},\qquad
\mathbb E[S(W_n)^2]\sim C_2(2r_2)^{-n},\qquad
\operatorname{Var}S(W_n)\sim C_2(2r_2)^{-n},
\]
where
\[
C_1=\frac{2}{-r_1 P_1'(r_1)}\approx1.38760048,\qquad
C_2=\frac{2(2-r_2-r_2^2+r_2^3)}{-r_2P_2'(r_2)}\approx2.21743002.
\]
In particular the coefficient of variation grows exponentially:
\[
\frac{\sqrt{\operatorname{Var}S(W_n)}}{\mathbb ES(W_n)}
\sim\frac{\sqrt{C_2}}{C_1}\left(\sqrt{\frac{2r_1^2}{r_2}}\right)^n,
\]
with prefactor approximately \(1.07315022\) and base approximately \(1.02167385\). Thus the relative mean-square deviation diverges; this moment calculation does not assert a limiting law or resolve concentration in probability.

## Assumptions and scope

Subsequences preserve order but need not be contiguous. Targets are counted without embedding multiplicities, and \(x,y\) mark zeros and ones of the source. Multivariate generating-function equalities are formal. The fixed-composition result includes constant and empty sources. The pole asymptotics are for the uniform model on all words, not for fixed composition.

## Proof

**Arch decomposition.** Read the source greedily from the left, ending each arch as soon as both letters occur. Every complete arch has the form \(b^r\bar b\), with \(r\ge1\) and \(\bar b=1-b\); the remainder is empty or constant. With \(m\) complete arches, every length-\(m\) target embeds by matching one symbol in each arch. The target formed from the last symbols of each arch followed by a letter missing from the remainder fails under leftmost greedy matching, and so is absent. Hence the shortest absent length is \(m+1\).

For a length-\(m+1\) target to be absent, each arch must consume exactly one symbol under greedy matching and the remainder must avoid the final target symbol. In fact, each complete arch consumes at least one if the target has not yet ended, so two consumed in any one arch would ensure completion by the end of the complete arches. Conversely, consumption of exactly one per arch leaves exactly one for the remainder. In an arch \(b^r\bar b\), if the current letter is \(\bar b\), it matches the last position and the next letter is unrestricted. If the current letter is \(b\), exactly one is consumed only if \(r=1\) and the next letter is also \(b\). This rule also applies to the last complete arch because the target has one extra letter.

**Single target.** Put \(u=xy\), \(L_0=xy/(1-y)\), \(L_1=xy/(1-x)\). With current states in order \(0,1\), the weighted transitions and terminal weights are
\[
T_1=\begin{pmatrix}L_0+u&L_0\\L_1&L_1+u\end{pmatrix},\qquad
v_1=\begin{pmatrix}(1-y)^{-1}\\(1-x)^{-1}\end{pmatrix}.
\]
For example, a current \(0\) can use an arch of the form \(1^r0\) and then either next letter; the additional option is the arch \(01\), forcing the next letter to be \(0\). A final \(0\) requires an empty or all-ones remainder. The source decomposition and the target determine the entire path. If \(p_0,p_1\) are the coordinates of \((I-T_1)^{-1}v_1\), the two equations take the form \((1-u)p_i-L_i(p_0+p_1)=(v_1)_i\). Summing gives
\[
F_1=p_0+p_1=\frac{(1-y)^{-1}+(1-x)^{-1}}{1-u-L_0-L_1},
\]
which gives the stated bivariate function after clearing denominators.

**Ordered target pairs.** Both targets must use the same source arch in each transition. Their current letters have four possible ordered states, and exchange symmetry allows the two mixed states to share one future-count coordinate. In order \(00,\text{mixed},11\), the matrix and terminal vector are
\[
T_2=\begin{pmatrix}
u+L_0&2L_0&L_0\\
u&2u&u\\
L_1&2L_1&u+L_1
\end{pmatrix},\qquad
v_2=\begin{pmatrix}(1-y)^{-1}\\1\\(1-x)^{-1}\end{pmatrix}.
\]
For instance, from state \(01\), arch \(01\) permits next states \(00,01\) and arch \(10\) permits \(01,11\), with no longer arches allowed. From state \(00\), the arches \(1^r0\) permit every next state; arch \(01\) adds the \(00\) transition. The \(11\) case follows by swapping symbols. A nonempty remainder cannot avoid both letters of a mixed terminal state. If \((p,h,s)^{\mathsf T}=(I-T_2)^{-1}v_2\), the initial weight row \((1,2,1)\) gives \(F_2=p+2h+s\). The rows give \((1-u)p=L_0F_2+(1-y)^{-1}\), \(h=uF_2+1\), and \((1-u)s=L_1F_2+(1-x)^{-1}\). Hence
\[
F_2=\frac{(1-y)^{-1}+(1-x)^{-1}+2(1-u)}{(1-u)(1-2u)-L_0-L_1}.
\]
Clearing denominators gives the stated bivariate function. Dividing coefficient totals by \(\binom nk\) gives the fixed-composition moments and variance.

**Diagonal specialization and poles.** Write \(u=z^2\) and \(L=z^2/(1-z)\). Swapping the binary letters leaves the diagonal transfers unchanged, so \(T_1\) reduces to the scalar \(2L+u\), with initial weight \(2\) and terminal weight \((1-z)^{-1}\). In the two-target case, one can set the two equal-letter future counts equal, to obtain the matrix, initial row and terminal column
\[
M=\begin{pmatrix}u+2L&2L\\2u&2u\end{pmatrix},\qquad
(2,2),\qquad \begin{pmatrix}(1-z)^{-1}\\1\end{pmatrix}.
\]
The two column sums of \(\operatorname{adj}(I-M)\) are \(1\) and \(1-u\), and \((1-z)\det(I-M)=P_2(z)\). Consequently
\[
F_1(z,z)=\frac{2}{P_1(z)},\qquad
F_2(z,z)=\frac{2[1+(1-z)(1-z^2)]}{P_2(z)}
=\frac{2(2-z-z^2+z^3)}{P_2(z)}.
\]
The coefficient of \(z^n\) divided by \(2^n\) gives the corresponding moment. The diagonal formulas also follow directly by canceling the factor \(1-z\) in each bivariate specialization.

For \(0<z<1\), the scalar and the Perron root of \(M(z)\) increase strictly from zero to above one; their derivatives are positive because their entries are strictly increasing and their Perron left and right vectors are positive. Each first reaches one at a simple zero of its denominator. At any complex \(z\) of the same modulus but not positive real, the loop with consecutive powers \(z^2,z^3\) gives strict triangle inequality in one entry, and all entries are bounded by their positive-real counterparts in modulus. Positivity of the real transfer gives spectral radius strictly below one there. The same entrywise bound gives spectral radius below one at all strictly smaller moduli. These facts give unique dominant poles. Evaluation at the rational interval endpoints above brackets the roots; in the bracket for \(P_2\), the smaller eigenvalue of \(M\) is below its diagonal entry \(2z^2<1\), so the sign change brackets the Perron crossing.

For a numerator \(N_j\) over \(P_j\) with a simple unique dominant pole \(r_j\), the leading coefficient is \(N_j(r_j)r_j^{-n}/[-r_jP_j'(r_j)]\). Applying this and the factor \(2^{-n}\) proves the two moment equivalents. Since \(r_2<0.406866<2(0.460811)^2<2r_1^2\), the square of the mean is exponentially smaller than the second moment. This proves the variance equivalent and the relative fluctuation formula.

## Verification

The accompanying standard-library `check_moments.py` (unchanged) checks coefficients of the bivariate functions against direct enumeration through length 14, checks the arch transfers through total degree 12, and verifies the fixed-composition example and positive-root brackets. It does not check the diagonal numerator or residues. To check the diagonal normalization at length one, the only sources are \(0\) and \(1\), each with a unique shortest absent target, so \([z]F_2(z,z)=2\). The full diagonal and residue computations are explicit in the proof above.

## Relationship to prior work and limitations

The shortest absent subsequence characterization and the arch framework are established in Kosche, Koß, Manea and Siemer. Adamson and coauthors study extremal counts, and Manea and coauthors study efficient enumeration. The length-only first-moment function \(2/P_1(z)\) is recovered here, not claimed as new. The result concerns aggregation over source words, in particular the second-moment transfer in which two targets must share every source arch. It gives no full distribution, fixed-composition asymptotic, or higher-alphabet formula. The exact second moment quantifies fluctuations across random sources that the first moment and worst-case bounds do not determine.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, Theorem 3.4 and the arch framework. https://arxiv.org/abs/2108.13968
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, Sections 3–5. https://arxiv.org/abs/2407.18599
3. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, Sections 1–6. https://arxiv.org/abs/2504.21471
