# Laguerre boundary law for polynomial projections on high-dimensional simplices

## Finding
Let \(P_{d,m}\) be the unweighted \(L^2\)-orthogonal projector onto polynomials of total degree at most \(m\) on a \(d\)-simplex, with normalized volume measure. At any vertex \(v\), its **sharp point-evaluation supremum norm** is
\[
V_{d,m}:=\sup_{\|f\|_\infty\le1}|(P_{d,m}f)(v)|
=d\int_0^1|k_{d,m}(t)|(1-t)^{d-1}\,dt,
\]
where \(k_{d,m}(t)=\sum_{j=0}^m a_jt^j\) is the uniquely determined polynomial satisfying
\[
\sum_{j=0}^m a_j\frac{(i+j)!}{(d+1)_{i+j}}=1\quad(0\le i\le m),\qquad (d+1)_r:=\prod_{k=1}^r(d+k).
\]
For every **fixed integer \(m\ge2\)** as \(d\to\infty\),
\[
\boxed{\lim_{d\to\infty}\frac{V_{d,m}}{d^m}
=\frac1{m!}\int_0^\infty e^{-s}|L_m(s)|\,ds>0,}\qquad
L_m(s)=\sum_{j=0}^m\frac{(-1)^j}{j!}\binom mj s^j.
\]
The vertex functional also has exact \(L^2\) norm \(\binom{d+m}{m}\); hence the ratio of its sharp \(L^\infty\) norm to its sharp \(L^2\) norm tends to \(\int_0^\infty e^{-s}|L_m(s)|\,ds\). The maximal loss of positivity **at that vertex**, for measurable inputs \(0\le f\le1\), is exactly \((V_{d,m}-1)/2\), and therefore grows as half the displayed constant times \(d^m\).

For \(m=2\), let
\[
a_d=\frac{2-\sqrt{2(d+2)/(d+3)}}{d+4},\quad
b_d=\frac{2+\sqrt{2(d+2)/(d+3)}}{d+4},
\]
\[
Q_d(t)=1-\frac{d^2(d+3)}2t+\frac{d(d+1)(d+3)(d+4)}4t^2.
\]
Then an **exact finite-dimensional formula** is
\[
\boxed{V_{d,2}=1+2\big[(1-b_d)^dQ_d(b_d)-(1-a_d)^dQ_d(a_d)\big].}
\]
In particular,
\[
\boxed{\lim_{d\to\infty}d^{-2}V_{d,2}
=\frac{(2-\sqrt2)e^{-(2-\sqrt2)}+(2+\sqrt2)e^{-(2+\sqrt2)}}{\sqrt2}
=0.310012507574629\ldots.}
\]
These are vertex evaluation results, **not a determination of the global \(\|P_{d,m}\|_{L^\infty\to L^\infty}\)**.

## Assumptions and scope
The simplex has \(d+1\) affinely independent vertices, \(d\ge1\), and carries uniform probability measure \(\mu_d\). Affine changes of variables preserve the claims. The projector is defined first in \(L^2(\mu_d)\) and extends by its continuous polynomial kernel to \(L^\infty(\mu_d)\) and \(C(\Delta_d)\). The limiting statements hold for each fixed \(m\ge2\), not jointly when \(m\) grows with \(d\). Every vertex has the same point-evaluation norm by barycentric symmetry.

## Proof
**1. Conditional reduction and the reproducing polynomial.** Write barycentric coordinates \(Y=(Y_0,\ldots,Y_d)\) of a uniform random point and select \(v\) with \(Y_0=1\). Then \(T:=Y_0\sim\operatorname{Beta}(1,d)\), with density \(d(1-t)^{d-1}\) on \((0,1)\). Conditional on \(T=t\), the other coordinates are \((1-t)Z\), where \(Z\) is uniform on the \((d-1)\)-simplex. Hence, for every polynomial \(p\) of total degree at most \(m\), \(q_p(t):=\mathbb E[p(Y)\mid T=t]\) is a polynomial of degree at most \(m\) and \(q_p(1)=p(v)\). The moment matrix \(H_{ij}=\mathbb E[T^{i+j}]=(i+j)!/(d+1)_{i+j}\), indexed by \(0\le i,j\le m\), is positive definite. Therefore there is a unique \(k_{d,m}\) obeying the moment equations in Finding. It satisfies
\[
\int k_{d,m}(Y_0)p(Y)\,d\mu_d(Y)
=\int k_{d,m}(t)q_p(t)\,d\operatorname{Beta}(1,d)(t)=q_p(1)=p(v).
\]
By uniqueness of the \(L^2\) representer, \(K_{d,m}(v,Y)=k_{d,m}(Y_0)\) is the full multivariate projection kernel at the vertex. Duality against \(L^\infty\) gives the exact formula for \(V_{d,m}\). Continuous functions approximating the sign of the kernel in \(L^1\) give the same supremum for \(C(\Delta_d)\).

**2. Sharp positivity defect.** The reproducing identity for constants yields \(\mathbb E[k_{d,m}(T)]=1\). The identity for \(1-T\), which vanishes at \(v\), yields \(\mathbb E[k_{d,m}(T)(1-T)]=0\). Since \(1-T>0\) a.s. and \(k\not\equiv0\), the kernel takes both signs on sets of positive measure for \(m\ge1\). Therefore
\[
\inf_{0\le f\le1}(P_{d,m}f)(v)
=\int_{k_{d,m}<0}k_{d,m}\,d\mu_d
=-\frac{V_{d,m}-1}{2}.
\]
The measurable indicator of the negative set attains this infimum; continuous functions approximate it arbitrarily closely. No continuous norm-one input attains \(V_{d,m}\), since equality would require the continuous input to equal the opposite constant signs on adjacent open regions separated by a zero hypersurface.

**3. Jacobi endpoint \(L^2\) norm.** Shifted Jacobi polynomials \(J_j(t)=P_j^{(d-1,0)}(2t-1)\) are orthogonal for the beta law, have \(\mathbb E[J_j(T)^2]=d/(d+2j)\) and \(J_j(1)=\binom{d+j-1}{j}\). Thus
\[
k_{d,m}(1)=\sum_{j=0}^m\frac{d+2j}{d}\binom{d+j-1}{j}^2
=\binom{d+m}{m}^2,
\]
where the last equality telescopes by consecutive binomial squares. The norm of evaluation on the \(L^2\) polynomial space is therefore \(\sqrt{k_{d,m}(1)}=\binom{d+m}{m}\).

**4. Laguerre scaling.** Put \(S_d=dT\) and \(h_{d,m}(s)=d^{-m}k_{d,m}(s/d)\). For \(0\le j\le m\),
\[
\mathbb E[h_{d,m}(S_d)S_d^j]=d^{j-m},\qquad
\mathbb E[S_d^r]=\frac{d^rr!}{(d+1)_r}\longrightarrow r!.
\]
The moment matrices of \(S_d\) converge entrywise to the positive-definite Hankel matrix \(((i+j)!)_{0\le i,j\le m}\). Solving these systems shows coefficientwise convergence to the unique polynomial \(h_m\) satisfying \(\int_0^\infty e^{-s}h_m(s)s^j\,ds=0\) for \(j<m\), and \(=1\) for \(j=m\). By the defining Laguerre orthogonality and its leading coefficient, \(h_m(s)=(-1)^mL_m(s)/m!\). The law of \(S_d\) converges to \(\operatorname{Exp}(1)\). Uniform boundedness of its moments of every fixed order, together with bounded coefficients of \(h_{d,m}\), makes \(|h_{d,m}(S_d)|\) uniformly integrable. Taking expectations proves the sharp \(d^m\) limit. Since \(\binom{d+m}{m}\sim d^m/m!\), the asserted \(L^\infty/L^2\) evaluation ratio follows.

**5. Quadratic exact specialization.** Solving the three beta moment equations gives
\[
k_{d,2}(t)=\frac{(d+1)(d+2)}4\big[(d+3)(d+4)t^2-4(d+3)t+2\big].
\]
Its roots are exactly \(a_d,b_d\), both in \((0,1)\), and it is negative precisely between them. Direct integration of the beta density gives
\[
\int_0^z k_{d,2}(t)d(1-t)^{d-1}\,dt=1-(1-z)^dQ_d(z).
\]
Subtracting at the roots yields the displayed finite formula. Finally \(L_2(s)=1-2s+s^2/2\), whose positive roots are \(2\pm\sqrt2\). Integrating \(e^{-s}|L_2(s)|/2\) across these intervals gives the explicit constant.

## Verification
The companion standalone script `verify_simplex_vertex.py` constructs the exact beta moment matrices, checks their reproducing equations and Jacobi diagonal identity for all integer pairs \(1\le d\le9\), \(1\le m\le5\), verifies the quadratic coefficients exactly, compares high-precision beta integrals with the algebraic quadratic formula for eight dimensions, and checks coefficientwise convergence for three fixed degrees at dimension 300. The analytic proof, rather than these finite experiments, establishes all quantified claims.

## Relationship to prior work
Classical simplex Jacobi polynomial constructions and recurrences underlie the reduction to a beta marginal. The cited 2011 simplex work develops orthogonal bases and singular Sobolev cases; the cited 2010 work develops multivariate recurrences; and the cited 2013 work proves boundary-trace and Sobolev estimates in fixed dimension. Those results provide relevant machinery, but no inspected statement supplies the fixed-degree, growing-dimension sharp **vertex \(L^\infty\) evaluation** law with its Laguerre constant and quadratic negativity profile. A published affine-simplex positivity-defect result covers degree one; it does not imply the higher-degree result because different polynomial projections need not preserve positivity or have monotone sharp endpoint norms.

## Limitations
This finding does not identify a global maximizing evaluation point, nor does it assert an exact global supremum-norm operator constant. The limiting argument keeps polynomial degree fixed. Classical Jacobi identities are essential prior ingredients; equivalent endpoint norm evaluations in older or unindexed orthogonal-polynomial literature are a residual originality risk. Continuous extremizers do not exist for the signed vertex kernel, although the operator norm remains its \(L^1\) kernel norm.

## References
1. R. Aktaş and Y. Xu, *Sobolev Orthogonal Polynomials on a Simplex*, arXiv:1111.2994v1 (public 2011-11-13), especially Sections 1–2, https://arxiv.org/abs/1111.2994.
2. S. Waldron, *Recursive Three-Term Recurrence Relations for the Jacobi Polynomials on a Triangle*, Technical Report dated 2010-03-03, Section 2; DOI:10.1007/s00365-010-9114-7.
3. J. M. Melenk and T. Wurzer, *On the stability of the boundary trace of the polynomial L²-projection on triangles and tetrahedra*, arXiv:1302.7189v1 (2013-02-28), Theorem 1.1, https://arxiv.org/abs/1302.7189.
4. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published research record dated 2026-10-04, published-finding corpus ID `99c2b9dd9b34`.
