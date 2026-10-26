# A sharp leaf–two-cycle covariance bound for heterogeneous random mappings

## Finding
Let \(n\ge2\), let \(p=(p_1,\ldots,p_n)\) be a probability vector with at least two positive coordinates, and let the outputs \(f(1),\ldots,f(n)\) be independent with \(\Pr\{f(i)=j\}=p_j\). Let \(Z\) be the number of vertices having no incoming arrows, \(T\) the number of directed two-cycles, and \(F\) the number of fixed points. Define
\[
 s_2=\sum_{i=1}^n p_i^2,\qquad
 W=\sum_{i=1}^n p_i(1-p_i)^{n-2},\qquad
 V=\sum_{i=1}^n p_i^2(1-p_i)^{n-2}.
\]
Then
\[
 \boxed{\operatorname{Cov}(Z,T)=\tfrac12\big((1+s_2)V-2s_2W\big)
 \ \le\ -\tfrac12s_2(1-s_2)W<0.}
\]
Equality in the displayed non-strict inequality holds if and only if \(n=2\) or all positive coordinates of \(p\) are equal. In addition, \(\operatorname{Cov}(Z,F)=0\) for every probability vector \(p\), including vectors supported at a single vertex. If \(p\) is supported at just one vertex, \(T\equiv0\), so the strict two-cycle statement does not apply.

This separates the exact zero covariance of sources with one-cycles from the universal, quantitatively bounded negative covariance with two-cycles, without requiring uniform target probabilities.

## Assumptions and scope
A functional digraph of \(f:[n]\to[n]\) has one outgoing arrow \(i\to f(i)\) at each vertex. A vertex is a source precisely when its indegree is zero; it need not be the root of a component. A two-cycle is an unordered pair \(\{i,j\}\), \(i\ne j\), with \(f(i)=j\) and \(f(j)=i\). A fixed point is \(f(i)=i\). The parameter \(n\) ranges over all integers at least two; the target probabilities are nonnegative and sum to one. In the strict statement, at least two are positive. Coordinates with probability zero are permitted, and count as deterministic sources. In the case \(n=2\), the exponent-zero expression \((1-p_i)^0\) is interpreted as one even at a zero base.

The law is a common-target or \(p\)-mapping law: all vertices use the same target vector, with independent choices. It is not a general array of origin-dependent transition probabilities.

## Proof
Put \(I_v=\mathbf 1\{v\notin f([n])\}\). Independence of the \(n\) outgoing choices gives
\[
 \mathbb E Z=\sum_v(1-p_v)^n.
\]
For distinct \(i,j\), the event \(A_{ij}=\{f(i)=j,f(j)=i\}\) has probability \(p_ip_j\). On this event, both \(i\) and \(j\) receive an incoming arrow. For \(v\notin\{i,j\}\), none of the two forced arrows points to \(v\), and the other \(n-2\) outputs remain independent, so
\[
 \mathbb E[Z\mathbf1_{A_{ij}}]
   =p_ip_j\sum_{v\ne i,j}(1-p_v)^{n-2}.
\]
Let \(e_2(p)=\sum_{i<j}p_ip_j=(1-s_2)/2\). Since \(T=\sum_{i<j}\mathbf1_{A_{ij}}\), finite summation gives
\[
 \mathbb ET=e_2(p),\qquad
 \mathbb E[ZT]=\sum_v(1-p_v)^{n-2}
       \big(e_2(p)-p_v(1-p_v)\big).
\]
Subtracting \(\mathbb EZ\,\mathbb ET\), and using \(1-(1-p_v)^2=p_v(2-p_v)\), yields
\[
 \begin{aligned}
 \operatorname{Cov}(Z,T)
 &=\sum_v p_v(1-p_v)^{n-2}
       \big(e_2(p)(2-p_v)-(1-p_v)\big)\\
 &=\tfrac12\sum_v p_v(1-p_v)^{n-2}
       \big((1+s_2)p_v-2s_2\big)\\
 &=\tfrac12\big((1+s_2)V-2s_2W\big).
 \end{aligned}
\]
To prove the sharp bound, regard \(P\) as a discrete random variable taking value \(p_i\) with probability \(p_i\). Then \(\mathbb EP=s_2\). The function \(h(t)=(1-t)^{n-2}\) is nonincreasing on \([0,1]\). For independent copies \(P,P'\),
\[
 2\operatorname{Cov}(P,h(P))
 =\mathbb E[(P-P')(h(P)-h(P'))]\le0.
\]
Consequently, \(V=\mathbb E[P h(P)]\le\mathbb EP\,\mathbb Eh(P)=s_2W\). Substituting into the exact identity gives
\[
 \operatorname{Cov}(Z,T)
 \le\tfrac12((1+s_2)s_2W-2s_2W)
 =-\tfrac12s_2(1-s_2)W.
\]
With at least two positive coordinates, \(0<s_2<1\) and \(W>0\), giving strict negativity. If \(n=2\), \(h\) is constant, so equality holds. If \(n>2\), \(h\) is strictly decreasing on the support of \(P\) (all positive coordinates are strictly below one), hence equality in the covariance inequality is equivalent to \(P\) being constant, i.e. all positive coordinates of \(p\) being equal. This completes the equality classification.

Finally, \(F=\sum_i\mathbf1\{f(i)=i\}\) has mean \(\mathbb EF=\sum_i p_i=1\). Conditional on \(I_v=1\), whenever \(p_v<1\), each of the \(n\) outputs is independently distributed on the other targets with probabilities \(p_j/(1-p_v)\). The fixed-point expectation is therefore \(\sum_{j\ne v}p_j/(1-p_v)=1\). If \(p_v=1\), the event \(I_v=1\) has probability zero. Thus \(\mathbb E[ZF]=\sum_v \mathbb P(I_v=1)\mathbb E[F\mid I_v=1]=\mathbb EZ\), establishing \(\operatorname{Cov}(Z,F)=0\).

## Verification
The standalone file `check_mapping_dependence.py` uses exact `fractions.Fraction` arithmetic. It enumerates all positive-probability mappings for 26 probability vectors in dimensions two through six, including uniform, strongly heterogeneous, and zero-probability target cases. It checks exact means, exact mixed covariances, strictness, the sharp bound, and all equality cases. It also checks further rational vectors in dimensions seven through twenty by exact formula arithmetic. The execution returned `PASS`, with 318 assertions and 150456 positive-probability mappings enumerated. These finite checks are diagnostic; the proof above covers all allowed dimensions and real probability vectors.

An illustrative instance is \(n=3\) and \(p=(1/3,1/3,1/3)\), when \(s_2=1/3\), \(W=2/3\), and \(\operatorname{Cov}(Z,T)=-2/27\), attaining the bound.

## Relationship to prior work
Finch, *Components and Cycles of Random Mappings* (first public version 2022-05-11), analyzes component and cycle-length observables in the uniform random-mapping model, not the heterogeneous-target sharp covariance inequality. Hansen and Jaworski, *Random Mappings With Exchangeable In-Degrees* (2008; first published online 2007), give a general formula for cyclic-point counts conditioned on an exchangeable indegree sequence. A nonuniform target vector normally has nonexchangeable indegrees, so their exchangeable-indegree theorem does not directly imply the present all-\(p\) bound. Their introductory general \(p\)-mapping definition and traditional counting framework are acknowledged. The new statement is specifically the strict sign and sharp lower bound on covariance magnitude for *all* common target vectors, with equality classification. The uniform specialization and fixed-point orthogonality alone are not presented as new.

## Limitations
No assertion is made for origin-dependent target arrays, for longer cycle counts, or for nonlinear conditional independence. A covariance sign is weaker than negative association. The proof is complete under the stated hypotheses; it does not establish historical priority. Existing general counting formulas or unpublished work might contain equivalent consequences. No independent mathematical audit has been performed.

## References
1. S. Finch, *Components and Cycles of Random Mappings*, arXiv:2205.05579, first posted 2022-05-11, https://arxiv.org/abs/2205.05579.
2. J. C. Hansen and J. Jaworski, *Random Mappings With Exchangeable In-Degrees*, Random Structures & Algorithms 33 (2008), 105–126, DOI:10.1002/rsa.20187.
3. J. C. Hansen and J. Jaworski, *Local Properties of Random Mappings With Exchangeable In-Degrees*, Advances in Applied Probability 40 (2008), 183–205, DOI:10.1239/aap/1208358892.
