# Two sharp quasi-stationary modal transitions in the three-site SIS contact process

## Finding
For the homogeneous exact continuous-time SIS contact process on the three-vertex path \(1-2-3\), the most likely *nonempty infected configuration conditioned on long-term nonextinction* changes exactly twice as the infection-to-recovery ratio \(\lambda\) increases:

- For \(0<\lambda<3/4\), only \(\{2\}\) maximizes the quasi-stationary probability.
- At \(\lambda=3/4\), all three singletons and both adjacent pairs are jointly maximal. Their five individual probabilities equal \(1/6\).
- For \(3/4<\lambda<\lambda_*\), precisely \(\{1,2\}\) and \(\{2,3\}\) are maximal.
- At \(\lambda=\lambda_*\), those two pairs tie with \(\{1,2,3\}\).
- For \(\lambda>\lambda_*\), only \(\{1,2,3\}\) is maximal.

The second boundary is \(\lambda_*=1.00924708262093\ldots\), the unique zero in \((3/4,5/4)\) of
\[
F(\lambda)=18\lambda^5-140\lambda^4+77\lambda^3+92\lambda^2-50\lambda+4.
\]
At \(\lambda=3/4\), the remaining probabilities are \(\pi(\{1,3\})=1/24\) and \(\pi(\{1,2,3\})=1/8\). The quasi-stationary extinction rate there is \(1/2\).

## Assumptions and scope
Fix \(\lambda>0\). Each infected vertex recovers independently at rate \(1\). Each edge from infected to susceptible transmits independently at rate \(\lambda\). There is no immigration, and the empty state is absorbing. All assertions concern the unique long-time distribution conditional on nonextinction, not a finite-time conditional distribution. One mode refers to the probability of one *labeled infected subset*, not the total probability of a cardinality class. The graph has three vertices with edges \(\{1,2\},\{2,3\}\); no other topology is claimed. The quasi-stationary distribution is independent of the initial nonempty infection set.

## Proof
The seven nonempty subsets communicate under the positive-rate transitions. Their transient generator is irreducible, so its Perron eigenvalue is \(-\theta\), where \(\theta>0\), and its normalized positive left eigenvector is the unique quasi-stationary law. Denote the probability of \(\{2\}\) by \(a\), either singleton endpoint by \(b\), either adjacent pair by \(c\), the disconnected endpoint pair by \(d\), and full infection by \(e\). Thus
\[
a+2b+2c+d+e=1,\qquad \theta=a+2b,\qquad 0<\theta<1.
\]
The second identity follows because extinction directly from a transient state can occur only by recovery of its sole infected vertex; positivity makes \(\theta<1\).

The exact incoming/outgoing balance equations \(\pi Q=-\theta\pi\) reduce to \(M(\lambda,\theta)(a,b,c,d,e)^T=0\), with
\[
M=\begin{pmatrix}
\theta-1-2\lambda&0&2&0&0\\
0&\theta-1-\lambda&1&1&0\\
\lambda&\lambda&\theta-2-\lambda&0&1\\
0&0&0&\theta-2-2\lambda&1\\
0&0&2\lambda&2\lambda&\theta-3
\end{pmatrix}.
\]
Put \(P(\lambda,\theta)=\det M(\lambda,\theta)\) and \(V=\operatorname{adj}(M)(1,0,0,0,0)^T\), with components \(V_a,V_b,V_c,V_d,V_e\). At the Perron root \(P=0\) this vector is a strictly positive multiple of \((a,b,c,d,e)\): in particular,
\[
V_c=-\lambda(\theta-2)(\theta-3-2\lambda)(\theta-1-\lambda)>0
\]
when \(\lambda>0\), \(0<\theta<1\). Hence the cofactor differences faithfully compare probabilities.

**First transition.** Direct exact elimination gives
\[
\begin{aligned}
\operatorname{Res}_{\theta}(P,V_a-V_b)&=8\lambda^9(\lambda-2)^2(\lambda+1)(4\lambda-3),\\
\operatorname{Res}_{\theta}(P,V_b-V_c)&=-16\lambda^8(\lambda-2)^3(\lambda+1)^3(4\lambda-3).
\end{aligned}
\]
At \(\lambda=2\) the only common root of either indicated pair is \(\theta=3\), outside the Perron range. At \(\lambda=3/4\), \(\theta=1/2\) is the admissible eigenroot, with normalized probabilities
\[
(a,b,c,d,e)=\left(\frac16,\frac16,\frac16,\frac1{24},\frac18\right).
\]
The implicit eigenvalue derivative at that point is \(\theta'=-6/17\), and the derivatives of \(V_a-V_b\) and \(V_b-V_c\) along the Perron branch are respectively \(-75/68\) and \(-375/68\). Because these differences can have no other positive-\(\lambda\) zeros on the Perron branch, for all \(0<\lambda<3/4\) one has \(a>b>c\), whereas for all \(\lambda>3/4\) one has \(c>b>a\).

**Full-infection transition and exclusion of the remaining pair.** The last two balance equations imply
\[
\frac dc=\frac{2\lambda}{(2-\theta)(3-\theta+2\lambda)}<1,
\qquad
\frac ec=\frac{2\lambda(2+2\lambda-\theta)}{(2-\theta)(3-\theta+2\lambda)}.
\]
Thus \(e>c\) if and only if \(4\lambda^2>(2-\theta)(3-\theta)\); any equality requires \(1/\sqrt2<\lambda<\sqrt{3/2}\). A further exact resultant is
\[
\operatorname{Res}_{\theta}(P,V_c-V_e)=8\lambda^{10}(\lambda-2)(\lambda+1)F(\lambda).
\]
The Sturm variation counts for \(F\) at \(7/10,3/4,5/4\) are respectively \(2,2,1\). Consequently \(F\) has no root between \(7/10\) and \(3/4\), and exactly one root in \((3/4,5/4)\). In the full possible equality range \((1/\sqrt2,\sqrt{3/2})\subset(7/10,5/4)\), this is the sole candidate. At \(\lambda=3/4\) one has \(e<c\), while at \(\lambda=5/4\) one has \(e>c\) because \(4\lambda^2>6>(2-\theta)(3-\theta)\). Continuity of the simple Perron eigenvector forces exactly one equality, at \(\lambda_*\). Therefore \(e<c\) below \(\lambda_*\), and \(e>c\) above it. Combining this with the strict order of \(a,b,c\) and \(d<c\) proves the complete mode classification, including both tie boundaries.

## Verification
Run `python verify_qsd.py` with SymPy and NumPy. It constructs \(M\) and its adjugate independently, verifies determinant substitution and the three elimination resultants exactly, checks the two spurious \(\theta=3\) roots, certifies the Sturm variation counts and derivative signs, and constructs the full seven-state Markov generator independently for numerical replay across all phases. The numerical replay tests examples only; the universal claims follow from the exact elimination, Sturm certificate and Perron arguments above. The file is provided in this package and requires no external datasets or code.

## Relationship to prior work
Peterson (2010) studies contact-process quasi-stationarity on large complete graphs with heterogeneous rates, not this small path. Zhang and Moura (2014) investigate a nonabsorbing, scaled SIS model and its most probable states; its transition law is not equivalent to the absorbing per-edge linear contact process. Economou, Gómez-Corral and López García (2015) give a general finite-network SIS Markov-chain and quasi-stationary eigenvector algorithm; they do not provide this exact three-site all-rate modal ordering or the two sharp thresholds in the examined QSD sections and examples. Overton and collaborators (2021/2022) study approximations to quasi-stationary mean infection statistics on networks, not this exact configuration-mode classification. The result uses these standard models and finite-state eigenvector principles as foundations; originality of any identical older small-network identity cannot be excluded without exhaustive historical access.

## Limitations
The theorem assumes exactly three vertices, homogeneous constant infection and recovery rates, exponential independent clocks, no external importation, and conditioning on indefinite survival. It does not establish an infinite-system phase transition, policy effectiveness, large-network asymptotics, or independence from historical equivalent calculations. The five-way tie is a probability identity for labeled states; cardinality-class modes behave differently. The value is an exact structural benchmark, not a calibrated epidemic forecast.

## References
- J. Peterson, *The contact process on the complete graph with random vertex-dependent infection rates* (first public May 5, 2010), https://arxiv.org/abs/1005.0810.
- C. Zhang and J. M. F. Moura, *Role of subgraphs in epidemics over finite-size networks under the scaled SIS process* (first public October 8, 2014), https://arxiv.org/abs/1410.2196.
- A. Economou, A. Gómez-Corral, M. López García, *A stochastic SIS epidemic model with heterogeneous contacts*, Physica A (2015), https://doi.org/10.1016/j.physa.2014.10.054; author manuscript https://eprints.whiterose.ac.uk/id/eprint/90144/1/Economou_et_al_2015.pdf.
- C. E. Overton, R. R. Wilkinson, A. Loyinmi, J. C. Miller, K. J. Sharkey, *Approximating quasi-stationary behaviour in network-based SIS dynamics*, Bulletin of Mathematical Biology (2022; online 2021), https://doi.org/10.1007/s11538-021-00964-7; full manuscript https://researchonline.ljmu.ac.uk/id/eprint/17176/1/ApproximatingQSDNetworkSIS_finalrevision.pdf.
