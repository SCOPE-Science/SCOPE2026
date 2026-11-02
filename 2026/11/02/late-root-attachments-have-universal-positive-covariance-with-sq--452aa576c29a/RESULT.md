# Late root attachments have universal positive covariance with squared magnetization

## Finding

Consider a uniformly grown random recursive tree with vertices \(1,\ldots,n\), and a two-spin broadcast with probability \(p\) of copying a parent's spin and probability \(1-p\) of reversing it. Put \(\theta=2p-1\in(-1,1)\). Let \(D_n\) be the root's number of children and \(X_n\) the sum of all \(n\) spins; its square does not depend on the root's initial spin. For \(j\ge2\), let \(I_j\) indicate that vertex \(j\) attaches directly to the root.

Define the explicitly computable quantities
\[
 \mu_m=\prod_{k=1}^{m-1}\left(1+\frac{\theta}{k}\right),\qquad
 d_1=1,\quad d_{m+1}=\left(1+\frac{2\theta}{m}\right)d_m+1,\qquad
 q_m=\mu_m-\frac{d_m}{m}.
\]
For \(j\ge3\), set \(b_{j,n}=\prod_{k=j}^{n-1}(1+2\theta/k)\), with empty product one. Then for all \(n\ge j\ge3\),
\[
 \operatorname{Cov}(I_j,X_n^2)
 =\frac{2\theta}{j-1}\,q_{j-1}\,b_{j,n}.
\]
For \(j=2,3\) this covariance is zero; for **every** \(n\ge j\ge4\) and \(\theta\ne0\), it is strictly positive, including the anticopying regime \(p<1/2\). Consequently
\[
 c_n(\theta):=\operatorname{Cov}(D_n,X_n^2)>0
 \quad(n\ge4,\;-1<\theta<1,\;\theta\ne0),
 \qquad c_4(\theta)=\frac{\theta^2(1-\theta)}9.
\]
At \(\theta=0\), \(c_n(0)=0\) for every \(n\). There are two sharp fixed-parameter asymptotic regimes:
\[
 \lim_{n\to\infty}c_n(\theta)=\frac1{1-2\theta}
 \quad(-1<\theta<0),
\]
whereas for \(0<\theta<1\), writing \(a_m=\prod_{k=1}^{m-1}(1+2\theta/k)\),
\[
 \lim_{n\to\infty}\frac{c_n(\theta)}{n^{2\theta}}
 =C(\theta):=\frac1{\Gamma(1+2\theta)}
 \sum_{j=2}^{\infty}\frac{2\theta\,q_j}{j\,a_{j+1}}
 \in(0,\infty).
\]
At the classical elephant-walk diffusion threshold \(\theta=1/2\) (equivalently \(p=3/4\)), this constant evaluates exactly to
\[
 \boxed{\displaystyle\lim_{n\to\infty}\frac{\operatorname{Cov}(D_n,X_n^2)}n
 =2-\frac{\pi^2}{6}.}
\]

## Assumptions and scope

For each integer \(j\ge2\), independently choose parent \(P_j\) uniformly from \(\{1,\ldots,j-1\}\). Give the root a fair spin \(\sigma_1\in\{-1,1\}\), and independently give every new edge a sign \(\eta_j\in\{-1,1\}\) with \(\Pr(\eta_j=1)=p\). Set \(\sigma_j=\eta_j\sigma_{P_j}\). The tree, edge signs and root spin are mutually independent. The theorem holds at every integer \(n\ge2\), fixed \(0<p<1\), and uses expectation over both tree and broadcast randomness. The squared sum \(X_n^2=(\sum_v\sigma_v)^2\) is unchanged if all spins are simultaneously reversed. For first moments only, normalize the root spin to \(+1\).

## Proof

**1. First and second moments.** With root-aligned spins, write \(M_m=\sigma_1 X_m\). Conditional on the full history through time \(m\),
\[
 \mathbb E[M_{m+1}-M_m\mid\mathcal F_m]
 =\frac{\theta}{m}M_m,
 \qquad
 \mathbb E[M_{m+1}^2\mid\mathcal F_m]
 =\left(1+\frac{2\theta}{m}\right)M_m^2+1.
\]
Therefore \(\mathbb EM_m=\mu_m\) and \(\mathbb E M_m^2=d_m\). The second recursion has the closed form
\[
 d_m=\frac{m-2\theta a_m}{1-2\theta}\quad(\theta\ne1/2),
 \qquad d_m=mH_m\quad(\theta=1/2),
\]
where \(a_m=\prod_{k=1}^{m-1}(1+2\theta/k)\) even when its first factor is nonpositive, and \(H_m=\sum_{k=1}^m1/k\). These identities follow by induction and remain well-defined at \(\theta=-1/2\).

**2. Sign of the root-versus-average discrepancy.** Direct subtraction gives
\[
 (m+1)q_{m+1}=(m+2\theta)q_m+
 (1-\theta+\theta/m)\mu_m-1,
 \qquad q_2=0.
\]
For each \(m\ge2\), let
\[
 f_m(t)=\log(1-t+t/m)+\sum_{k=1}^{m-1}\log(1+t/k),\qquad -1<t<1.
\]
It is strictly concave, with \(f_m(0)=f_m(1)=0\) (the latter by continuous evaluation at the endpoint). Hence \(f_m(t)>0\) for \(0<t<1\); strict concavity and interpolation of zero between \(t<0\) and \(1\) give \(f_m(t)<0\) for \(-1<t<0\). Thus \((1-\theta+\theta/m)\mu_m-1=e^{f_m(\theta)}-1\) has the sign of \(\theta\). Because \((m+2\theta)/(m+1)>0\), induction shows that \(q_m\) has the strict sign of \(\theta\) for all \(m\ge3\), and vanishes identically when \(\theta=0\).

**3. Exact attachment profile.** For \(j\ge3\), condition on \(\mathcal F_{j-1}\) and on whether \(P_j=1\). The conditional expectations of the new root-aligned spin are respectively \(\theta\) and \(\theta(M_{j-1}-1)/(j-2)\). Since the squared spin increment equals one,
\[
 \operatorname{Cov}(I_j,M_j^2)
 =\frac{2\theta}{j-1}\left(\mu_{j-1}-\frac{d_{j-1}}{j-1}\right)
 =\frac{2\theta}{j-1}q_{j-1}.
\]
All future conditional squared moments are affine in \(M_j^2\), with coefficient \(b_{j,n}=\prod_{k=j}^{n-1}(1+2\theta/k)\). Every factor in this product is positive for \(j\ge3\) and \(-1<\theta<1\). This proves the stated profile and its sign. The indicator \(I_2\) is deterministic, and \(q_2=0\) handles \(I_3\). Summing over \(D_n=\sum_{j=2}^n I_j\) proves strict total covariance for \(n\ge4\); setting \(n=4\) yields the exact stated expression.

**4. Negative-bias limit.** From the first-moment product, \(\mu_m\to0\) when \(-1<\theta<0\). The closed second-moment form gives \(d_m/m\to(1-2\theta)^{-1}\), since \(a_m\to0\) (including its possible zero factor). Consequently \(q_m\to-(1-2\theta)^{-1}\). The covariance recursion derived from Step 3 is
\[
 c_{m+1}=\left(1+\frac{2\theta}{m}\right)c_m
 +\frac{2\theta}{m}q_m,\qquad c_2=0.
\]
Its homogeneous product decays to zero for negative \(\theta\), and the driving term approaches the unique stable balance \(c=(1-2\theta)^{-1}\). Explicitly, subtract that balance, expand the recurrence, and apply weighted Cesàro convergence using positive factors from \(m\ge2\). This proves the negative-bias limit.

**5. Positive-bias limit.** For \(0<\theta<1\), \(\mu_m\sim m^{\theta}/\Gamma(1+\theta)\). The second-moment expression shows \(d_m/m=o(\mu_m)\): it is bounded for \(\theta<1/2\), grows logarithmically at \(\theta=1/2\), and is of order \(m^{2\theta-1}\) for \(\theta>1/2\). Hence \(q_m\sim\mu_m>0\). Divide the covariance recursion by \(a_{m+1}\) and telescope:
\[
 \frac{c_n}{a_n}=\sum_{j=2}^{n-1}\frac{2\theta\,q_j}{j\,a_{j+1}}.
\]
The summand is positive and asymptotic to a constant times \(j^{-1-\theta}\), so its infinite sum converges strictly between zero and infinity. As \(a_n\sim n^{2\theta}/\Gamma(1+2\theta)\), the positive-bias limit follows.

**6. Explicit critical constant.** For \(\theta=1/2\), \(a_m=m\), \(d_m=mH_m\), and
\[
 \mu_m=\frac{2m}{4^m}{2m\choose m}.
\]
The series for \(C(1/2)\) becomes
\[
 \sum_{m=2}^{\infty}\frac{\mu_m-H_m}{m(m+1)}.
\]
Writing \(\mathrm{Cat}_m={2m\choose m}/(m+1)\) and using the Catalan generating function at \(1/4\),
\[
 \sum_{m=1}^{\infty}\frac{\mu_m}{m(m+1)}
 =2\sum_{m=1}^{\infty}\frac{\mathrm{Cat}_m}{4^m}=2.
\]
Swapping nonnegative sums also gives
\[
 \sum_{m=1}^{\infty}\frac{H_m}{m(m+1)}
 =\sum_{k=1}^{\infty}\frac1{k^2}=\frac{\pi^2}{6}.
\]
The \(m=1\) terms cancel in the difference, proving \(C(1/2)=2-\pi^2/6\).

## Verification

The accompanying standalone `CHECK.py` independently enumerates every labeled recursive tree through order eight for seven rational broadcast correlations, computing the conditional quadratic spin moment directly as \(\sum_{u,v}\theta^{\operatorname{dist}_T(u,v)}\), not by using the moment recurrence being checked. It compares exact rational total covariances and every individual arrival contribution against the formulas, and additionally checks the finite critical-parameter and four-vertex identities. Run `python CHECK.py` with Python 3 standard library. The current exact run passed **399 assertions**. This finite verification does not certify the infinite-size limits; Steps 4–6 provide those proofs.

## Relationship to prior work

Kürsten (2015 preprint, published 2016) identifies the elephant-walk/recursive-tree coupling and derives its first two displacement moments, including the diffusion threshold. Desmarais, Holmgren and Wagner (first posted 2021) analyze broadcast color counts, monochromatic clusters and color-dependent fringe statistics on recursive and preferential-attachment trees. Addario-Berry, Devroye, Lugosi and Velona (2020) study root reconstruction from broadcast spins. None of their inspected results states the joint genealogy–quadratic-displacement covariance, its all-generation positive sign on both sides of the copy threshold, or the exact critical constant above. Prior work on root-degree correlations with root *percolation-cluster size* concerns a different random observable: the quadratic magnetization includes correlations between every pair of spin sites, not merely the root cluster. A title or keyword mismatch is not proof of priority; historical overlap remains possible.

## Limitations

The result concerns uniform recursive attachment, a common edge-copy probability strictly between zero and one, and the square of the **total** spin sum. It does not establish stochastic monotonicity under forcing attachments, a central limit theorem for the covariance, the optimality of the finite-size constants in other models, or a formula for conditional full distributions given root degree. The asymptotic statements keep \(\theta\) fixed; no uniformity is claimed near \(\theta=0\) or the deterministic endpoint. Independent mathematical validation and definitive priority review are not available.

## References

- R. Kürsten, *Random Recursive Trees and the Elephant Random Walk*, arXiv:1512.05275, first posted 16 December 2015; *Physical Review E* **93** (2016), 032111. https://arxiv.org/html/1512.05275v1
- C. Desmarais, C. Holmgren and S. Wagner, *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050, first posted 28 October 2021. https://arxiv.org/abs/2110.15050
- L. Addario-Berry, L. Devroye, G. Lugosi and V. Velona, *Broadcasting on random recursive trees*, arXiv:2006.11787, first posted 21 June 2020. https://arxiv.org/abs/2006.11787
