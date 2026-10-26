# Universal transport plans and affine Lipschitz-free norms for independently weighted multipartite metrics

## Finding

Let a finite set be partitioned into \(r\ge 2\) nonempty parts \(M=A_1\sqcup\cdots\sqcup A_r\), with no restriction on the part sizes. For any vector \(\mathbf t=(t_1,\ldots,t_r)\in[1,2]^r\), put distance \(1\) between different parts and distance \(t_i\) between distinct points of \(A_i\). For every real signed measure \(\mu\) on \(M\) with total mass zero, define
\[
P=\sum_{x\in M}\mu(x)_+=\frac12\sum_{x\in M}|\mu(x)|,
\qquad U_i=\sum_{x\in A_i}|\mu(x)|.
\]
Then the exact transportation, or real Lipschitz-free, norm is
\[
\boxed{\|\mu\|_{\mathcal F(M,d_{\mathbf t})}
=P+\max_{1\le i\le r}(t_i-1)(U_i-P)_+.}
\]
At most one term \((U_i-P)_+\) is nonzero. More strongly, **there exists one transport coupling for \(\mu\) that is optimal for every** \(\mathbf t\in[1,2]^r\) simultaneously. Consequently, for every pair of parameter vectors \(\mathbf s,\mathbf t\in[1,2]^r\), every \(\theta\in[0,1]\), and every such \(\mu\),
\[
\boxed{\|\mu\|_{\mathcal F(M,d_{(1-\theta)\mathbf s+\theta\mathbf t})}
=(1-\theta)\|\mu\|_{\mathcal F(M,d_{\mathbf s})}
+\theta\|\mu\|_{\mathcal F(M,d_{\mathbf t})}.}
\]
This is affine interpolation of the **entire norm at each fixed vector**, not an asserted affine identity between unit balls. Both identities include the boundary values \(t_i=1\) and \(t_i=2\), singleton parts, and \(\mu=0\).

## Assumptions and scope

All measures, functions, and Banach spaces are real. The metric is \(d(x,x)=0\); for distinct \(x,y\), \(d(x,y)=t_i\) if \(x,y\in A_i\) and \(d(x,y)=1\) otherwise. The triangle inequality follows from \(1\le t_i\le2\). Fix any basepoint of \(M\); the real Lipschitz-free space has the standard model of total-mass-zero signed measures with
\[
\|\mu\|_{\mathcal F(M,d)}
=\max_{|f(x)-f(y)|\le d(x,y)}\sum_{x\in M}\mu(x)f(x).
\]
Equivalently, write \(\mu=\mu^+-\mu^-\) and minimize the total travel cost over nonnegative couplings with outgoing masses \(\mu^+\) and incoming masses \(\mu^-\). All assertions are for arbitrary finite part sizes, arbitrary independently chosen real parameters \(\mathbf t\in[1,2]^r\), and arbitrary real coefficients of \(\mu\) of total mass zero; there is no rationality hypothesis.

## Proof

**1. A unique possible overloaded part.** Put \(P_i=\mu^+(A_i)\) and \(N_i=\mu^-(A_i)\). Then \(\sum_iP_i=\sum_iN_i=P\), and \(U_i=P_i+N_i\). Since \(\sum_iU_i=2P\), at most one index satisfies \(U_i>P\). Call its excess \(\delta=U_i-P>0\), if it exists. Set \(\delta=0\) otherwise. For \(P=0\), necessarily \(\mu=0\) and the theorem is immediate.

**2. A coupling with the minimum possible within-part mass.** Consider a bipartite network whose source vertices are points with \(\mu(x)>0\), whose target vertices are points with \(\mu(y)<0\), and whose allowed edges join **different** parts. A source subset meeting at least two parts is adjacent to every target; a source subset lying inside one part \(A_i\) sees all negative mass except \(N_i\). The fractional Hall condition for complete shipment across parts is therefore exactly
\[
P_i\le P-N_i\quad\text{for every }i,
\quad\text{equivalently}\quad U_i\le P\quad\text{for every }i.
\]
If this condition holds, a nonnegative cross-part coupling carries all mass \(P\), at cost exactly \(P\) for **every** parameter vector.

If it fails, exactly one part \(A_i\) has \(\delta=P_i+N_i-P>0\). Send \(P-N_i\) units of positive mass from \(A_i\) to **all** negative mass outside \(A_i\), and send all \(P-P_i\) units of positive mass outside \(A_i\) to negative mass in \(A_i\). These shipments are possible because \(P_i\ge P-N_i\) and \(N_i\ge P-P_i\), respectively. They carry \(P-\delta\) units across parts, leaving exactly \(\delta\) positive and \(\delta\) negative mass inside \(A_i\). Ship the residual directly inside \(A_i\). The resulting coupling has cost
\[
(P-\delta)+t_i\delta=P+(t_i-1)\delta.
\]
This construction uses only the source and target masses, not the values of any \(t_j\). Thus **the same coupling** attains this upper bound across the whole parameter cube.

**3. Matching dual lower bounds.** When \(\delta=0\), let \(f=1\) on the positive support of \(\mu\) and \(f=0\) elsewhere. This is one-Lipschitz because every distance between different points is at least \(1\), and its pairing with \(\mu\) equals \(P\).

When \(\delta>0\) in part \(A_i\), define \(f\) by the following values on supports: inside \(A_i\), put \(f=t_i\) at positive-mass points and \(f=0\) at negative-mass points; outside \(A_i\), put \(f=1\) at positive-mass points and \(f=t_i-1\) at negative-mass points. At zero-mass points take \(f=0\) inside \(A_i\) and \(f=t_i-1\) outside. Within \(A_i\) the variation is at most \(t_i\); within any other part it is at most \(2-t_i\le1\le t_j\); and every cross-part difference is at most \(1\), because \(1\le t_i\le2\). Thus \(f\) is one-Lipschitz. Its pairing is exactly
\[
\begin{aligned}
\sum_x\mu(x)f(x)
&=t_iP_i+(P-P_i)-(t_i-1)(P-N_i)\\
&=P+(t_i-1)(P_i+N_i-P)\\
&=P+(t_i-1)\delta.
\end{aligned}
\]
This matches the coupling upper bound for every parameter vector. Since at most one \(U_i-P\) can be positive, the displayed exact norm formula follows for all cases.

**4. Simultaneous optimality and affinity.** The coupling of Step 2 depends on \(\mu\) and its cluster supports, but not on the parameter vector. Its total cost equals the optimal norm simultaneously for every \(\mathbf t\in[1,2]^r\). The cost of a fixed coupling is affine in each \(t_i\), so the interpolation identity in the finding follows. \(\square\)

## Verification

The full proof uses the fractional Hall criterion and an explicit matching dual potential for **arbitrary real mass vectors**, hence does not depend on finite tests. The independent Python standard-library program `check_transport.py` exhausts zero-sum masses with entries in \(\{-1,0,1\}\) on five heterogeneous multipartite configurations; it computes every small transport optimum by exact rational permutation enumeration, compares the claimed formula, and checks affine interpolation at a second independent parameter vector. Run `python3 check_transport.py`; the observed result is `MULTIPARTITE_TRANSPORT_EXACT_OK cases=745 norm_affinity_checks=745`. This corroborates the formula, but its finite sample is not a proof of any infinite or continuous quantifier.

For a nontrivial illustration, let \(\mu\) on three nonempty parts have mass \(+2\) and \(-2\) at different points of the first part, mass \(+1\) at a point of the second part, and mass \(-1\) at a point of the third. Here \(P=3\) and the first part alone has \(U_1=4\), hence the cost is \(2+t_1\), irrespective of the other intrapart distances. Exactly one unit must be routed inside the first part; the other two units can cross between parts.

## Relationship to prior work

Higashitani, Jochemko and Michałek (2018, Section 3.1, particularly Propositions 3.4–3.5) classify facets of symmetric edge polytopes for complete bipartite and multipartite **unit-edge graph metrics**. Those describe the endpoint with all intrapart distances equal to \(2\), not the joint multi-parameter transportation norm. Aliaga and Pernecká (2018) develop extreme-molecule geometry in Lipschitz-free spaces, while Alexander, Fradelizi, García-Lirola and Zvavitch (2019) treat geometric structure and finite-metric decompositions; neither supplies the present coupling/affinity formula.

A later published mathematical classification of facets for interpolated multipartite metrics with **one common** intrapart distance, and its separate two-part analogue, provides closely related dual-polytope information. Those full statements classify facets/dual extreme potentials, not optimal transport couplings across **arbitrary independent** intrapart distances. For a common distance, a norm formula may be recoverable from those stronger dual classifications; the equal-parameter specialization is **not asserted as independently new**. A published clustered-space projection formula for within-part distances at most \(1\) optimizes a different operator on a different parameter domain. The contribution assessed here is the independent-parameter, common-optimal-coupling and pointwise-affinity theorem. These mathematical comparisons do not amount to proof of uniqueness in the literature.

## Limitations

The result requires finite multipartite metrics with a single constant distance within each part, cross-part distances identically \(1\), all intrapart distances in \([1,2]\), and real zero-total-mass measures. It does not describe general weighted cross edges, within-part nonconstant distances, optimal plans for \(W_p\) with \(p>1\), or unbalanced transportation. Multiple optimal plans may exist, especially at parameter boundaries; only the **existence** of one parameter-independent optimal plan is established. An equivalent formulation in older, incompletely indexed transport or Lipschitz-free literature remains a bibliographic risk. Independent mathematical assessment has not been performed.

## References

1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, first public 20 July 2018, Section 3.1. https://arxiv.org/html/1807.07678v1
2. R. J. Aliaga, E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278v1, first public 26 October 2018. https://arxiv.org/abs/1810.11278
3. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1, first public 24 November 2019. https://arxiv.org/abs/1911.10642
