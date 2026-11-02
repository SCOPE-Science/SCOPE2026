# Exact product laws for rank-one matrix idempotents over finite fields

## Finding

Let \(q\) be any prime power, \(n\ge 2\), and \(k\ge1\). Sample independent, uniformly distributed rank-one idempotents \(E_1,\ldots,E_k\) in \(M_n(\mathbb F_q)\), and write \(P_k=E_1\cdots E_k\). Put
\[
N=\frac{q^n-1}{q-1},\qquad a=\frac{q^{n-1}}N,\qquad b=\frac1{qN},\qquad C_k=a^k+(N-1)b^k,\qquad D_k=N^{1-k}.
\]
Here \(N\) is the number of projective lines in \(\mathbb F_q^n\). The complete distribution, including the probability of every individual target matrix, is as follows:
\[
\Pr(P_k=0)=1-a^{k-1}.
\]
For a nonzero matrix \(X\) of rank one, write \(\lambda=\operatorname{tr}(X)\). Then
\[
\Pr(P_k=X)=
\begin{cases}
\displaystyle\frac{a^{k-1}-C_k}{N(q^{n-1}-1)}, &\lambda=0,\\[2mm]
\displaystyle\frac{(C_k-D_k)/(q-1)+D_k\mathbf1_{\{\lambda=1\}}}{Nq^{n-1}}, &\lambda\ne0.
\end{cases}
\]
Every target of rank at least two has probability zero. In particular, the exact nilpotent-product probability is
\[
\boxed{\Pr(P_k\text{ is nilpotent})=1-C_k.}
\]
The probability that \(P_k\) is nonzero and nilpotent is \(a^{k-1}-C_k\); whenever this happens, \(P_k^2=0\).

The nonzero trace distribution exhibits an exact exceptional bias:
\[
\Pr(\operatorname{tr}P_k=1)-\Pr(\operatorname{tr}P_k=t)=D_k
\quad(t\in\mathbb F_q^\times,\ t\ne1).
\]
The latter difference refers to unconditional probabilities. For \(q=2\) it is vacuous because no such \(t\) exists.

Conditioned on \(P_k\ne0\), the law converges to the uniform distribution \(U\) on all nonzero rank-one matrices. More precisely,
\[
\boxed{\left\|\mathcal L(P_k\mid P_k\ne0)-U\right\|_{\mathrm{TV}}
=\frac{(N-1)b^k+(q-2)D_k}{(q-1)a^{k-1}}.}
\]
The displayed quantity tends to zero as \(k\to\infty\). Thus a product of rank-one idempotents, conditional on remaining nonzero, asymptotically loses its idempotent bias and becomes uniform on the entire nonzero rank-one class.

## Assumptions and scope

All fields are finite, all products are ordinary matrix products, and sampling is uniform **among rank-one idempotents**, not among all matrices, all rank-one matrices, or all idempotents. The factors are independent and ordered. The zero matrix is nilpotent of index one; any other nilpotent matrix that can arise here has index exactly two. The theorem holds for every integer \(k\ge1\) and \(n\ge2\), including characteristic two and nonprime fields. The restriction \(n\ge2\) ensures that nonzero rank-one square-zero targets exist; the one-dimensional case is deterministic and omitted.

## Proof

**1. Projective parameterization.** For each projective line \(L\subset V=\mathbb F_q^n\), fix a nonzero representative \(u_L\). Every rank-one idempotent with image \(L\) is uniquely \(u_Lf\), where \(f:V\to\mathbb F_q\) is linear and \(f(u_L)=1\). There are exactly \(q^{n-1}\) admissible forms per line. Hence the total number of sampled matrices is \(Nq^{n-1}\), and a uniform sample is equivalent to choosing a line uniformly then an admissible form uniformly.

For a sequence \((L_i,f_i)_{i=1}^k\), multiplication gives
\[
P_k=\left(\prod_{i=1}^{k-1}f_i(u_{L_{i+1}})\right)u_{L_1}f_k,
\qquad
\operatorname{tr}P_k=\prod_{i=1}^kf_i(u_{L_{i+1}}),\quad L_{k+1}=L_1.
\]
In particular, all outputs have rank at most one.

**2. Probability of a nonzero product.** Given any nonzero linear form \(f\), precisely \(q^{n-1}\) of the \(N\) projective lines are not contained in \(\ker f\): indeed, there are \(q^n-q^{n-1}\) nonzero vectors outside the hyperplane, each line containing \(q-1\) of them. Thus, independently of the previous nonzero product, multiplying by a fresh uniform rank-one idempotent preserves nonzeroness with probability \(a=q^{n-1}/N\). By induction,
\(\Pr(P_k\ne0)=a^{k-1}\), proving the formula at zero.

**3. Nonzero trace and the two-eigenvalue transfer operator.** Given adjacent image lines \(L,L'\), the probability that \(f(u_{L'})\ne0\) for a uniform form satisfying \(f(u_L)=1\) is one if \(L=L'\), and \(1-q^{-1}\) if \(L\ne L'\). For a fixed cyclic line sequence these events are independent, as distinct forms are sampled independently. Let \(H\) be the \(N\)-by-\(N\) matrix with diagonal entries one and off-diagonal entries \(1-q^{-1}\). Then
\[
\Pr(\operatorname{tr}P_k\ne0)=N^{-k}\operatorname{Tr}(H^k).
\]
Since \(H=q^{-1}I+(1-q^{-1})J\), its eigenvalues are \(q^{n-1}\) (once) and \(q^{-1}\) (with multiplicity \(N-1\)); here \(1+(q-1)N=q^n\). Therefore this probability is exactly \(C_k=a^k+(N-1)b^k\). A nonzero rank-one matrix is nilpotent precisely when its trace is zero, so total nilpotence probability is \(1-C_k\), while nonzero nilpotence has mass \(a^{k-1}-C_k\).

**4. Nontrivial multiplicative characters and trace-one bias.** Let \(\chi\ne1\) be a multiplicative character of \(\mathbb F_q^\times\), extended by \(\chi(0)=0\). Conditional on \(L\ne L'\), the scalar \(f(u_{L'})\) is uniform on \(\mathbb F_q\), so \(\mathbb E\chi(f(u_{L'}))=0\). If \(L=L'\), the scalar equals one. Hence in the cyclic product all character expectations vanish unless all image lines coincide. That event has probability \(N^{1-k}=D_k\). We obtain
\[
\mathbb E\chi(\operatorname{tr}P_k)=D_k\quad\text{for every nontrivial }\chi.
\]
Orthogonality of multiplicative characters, including the trivial character extended by zero, implies for each \(t\ne0\):
\[
\Pr(\operatorname{tr}P_k=t)=\frac{C_k-D_k}{q-1}+D_k\mathbf1_{\{t=1\}}.
\]
For \(q=2\), the same formula follows directly from the sole nonzero trace value, without nontrivial characters.

**5. Individual target probabilities.** Conjugating every independent sampled factor by the same element of \(\mathrm{GL}_n(\mathbb F_q)\) leaves the joint law unchanged. All nonzero rank-one matrices of a fixed trace form a single conjugacy orbit: for nonzero trace \(t\), such matrices are scalar multiples of rank-one idempotents, while all nonzero rank-one matrices with trace zero are square-zero and have one Jordan block of size two. There are \(Nq^{n-1}\) matrices of each prescribed nonzero trace, and \(N(q^{n-1}-1)\) nonzero rank-one matrices of trace zero, by the same \(u_Lf\) parameterization without normalizing \(f(u_L)\) to one. Dividing each trace-class mass by its orbit size proves the displayed exact pointwise distribution.

**6. Exact conditional mixing.** There are \(N(q^n-1)\) nonzero rank-one matrices. Under their uniform law, trace zero has mass \(1-a\), and each nonzero trace has mass \(a/(q-1)\). Under the product law conditioned on \(P_k\ne0\), trace zero has a deficit \((N-1)b^k/a^{k-1}\); each trace \(t\ne0,1\) has a deficit \([D_k-(N-1)b^k]/[(q-1)a^{k-1}]\), which is nonnegative because \(D_k>(N-1)b^k\). Only trace one has positive excess, equal to \([(N-1)b^k+(q-2)D_k]/[(q-1)a^{k-1}]\). Since both laws are uniform on each conjugacy orbit, the total variation distance equals this excess. This proves the last formula and convergence, since \(0<b<a<1\) and \(D_k/a^{k-1}=q^{-(n-1)(k-1)}\).

## Verification

Two standalone Python programs, supplied with this finding, perform independent exact checks. `CHECK.py` enumerates all rank-one idempotents and their actual matrix products, tracking every ordered word through lengths seven over \(\mathbb F_2\) in dimension two, six over \(\mathbb F_3\) in dimension two, and five over \(\mathbb F_2\) in dimension three. Its checks include pointwise target masses, the zero/nilpotent decomposition, trace probabilities, a separately enumerated projective-cycle transfer calculation, and exact total-variation distances. `CHECK_GF4.py` independently implements arithmetic in \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), checks all matrix products through length five in dimension two, and compares every nonzero trace mass and the zero mass. Both return `VERIFY_OK`; outputs are included. Exhaustive finite tests corroborate, but do not replace, the proof for all prime powers, dimensions, and lengths.

## Relationship to prior work

Sarma and Subedi (2026) introduced nilpotent-product probability for two uniformly sampled **arbitrary ring elements** and analyzed several ring classes. The present measure samples a much smaller, geometrically defined conjugacy class, allows every word length, and determines the complete resulting matrix law and its exact conditional uniformization.

Ferraz, Polcino Milies, and Taufer (2017) counted rank-one idempotent generators of minimal left ideals in a full finite-field matrix ring (\(q^{n-1}\) per line). This supplies the natural geometric parameterization but does not state the product-word distribution.

Holmes and Im (2026) determined nilpotency probabilities for cyclic-quiver representations using unrestricted linear maps. Their strong result already covers products of arbitrary independent random square matrices, and no claim of novelty is made for that unrestricted calculation. Conditioning **every factor** to be an idempotent imposes the additional constraints \(f_i(u_i)=1\) absent from the unrestricted quiver result; these produce the exceptional trace-one atom and the sharp total-variation formula.

Classical work of Erdős on products of idempotent matrices addresses factorability, rather than this uniform random-word distribution. Related 2026 work of Dolžan on nilpotent/idempotent matrix factorizations addresses specific factorization classes. No unconditional proof of historical priority is asserted.

## Limitations

This is a result for **rank-one** idempotents only, not idempotents of higher rank, arbitrary projectors, or uniformly sampled elements of the full matrix ring. Nothing is claimed about the distribution of the first hitting time of nilpotence, because nilpotence is not necessarily preserved under later right multiplication. The proof is symbolic; exact finite-field computations are corroboration, not an infinite certification. The originality assessment is based on the accessible literature and searchable mathematical records, not an exhaustive historical survey; the full text of every older idempotent-product source could not be inspected.

## References

- D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1, 6 October 2026, https://arxiv.org/html/2610.07892v1.
- R. A. Ferraz, C. Polcino Milies, and E. Taufer, *Left Ideals in Matrix Rings over Finite Fields*, arXiv:1711.09289v1, 25 November 2017, https://arxiv.org/html/1711.09289v1.
- C. Holmes and M. S. Im, *Nilpotent Representations over Equioriented Cyclic Quivers*, arXiv:2608.16636v1, 17 August 2026, https://arxiv.org/abs/2608.16636.
- D. Dolžan, *Products of Nilpotent and Idempotent Matrices over Finite Local Rings*, arXiv:2608.20934, 21 August 2026, https://arxiv.org/abs/2608.20934.
- J. A. Erdős, *On Products of Idempotent Matrices*, Glasgow Mathematical Journal (1967), https://doi.org/10.1017/S0017089500000173.
