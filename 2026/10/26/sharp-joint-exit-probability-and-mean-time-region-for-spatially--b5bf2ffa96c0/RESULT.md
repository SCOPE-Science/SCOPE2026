# Sharp joint exit-probability and mean-time region for spatially heterogeneous persistent transport

## Finding

Let \(L,v>0\). A particle starts at \(x=0\) with velocity \(+v\) directed into \([0,L]\); its velocity reverses at local rate \(\lambda(x)\ge0\), where \(\lambda\in C([0,L])\), and is absorbed on subsequent arrival at either endpoint. Write \(p\) for the right-exit probability and \(\tau\) for its mean absorption time. With \(K=v^{-1}\int_0^L\lambda(x)\,dx\) and \(B=v^{-1}\int_0^L x\lambda(x)\,dx\), exactly \(p=(1+K)^{-1}\) and \(\tau=p(L+2B)/v\). As \(\lambda\) varies, the complete attainable set of pairs is \(\{(1,L/v)\}\cup\{(p,\tau):0<p<1,\ pL/v<\tau<(2-p)L/v\}\). Every interior pair is attained by a strictly positive smooth rate, whereas both bounds at fixed \(0<p<1\) are sharp and unattained. The joint observations \((p,\tau)\) determine exactly the zeroth and first spatial rate moments but leave infinitely many distinct positive smooth profiles indistinguishable.

## Assumptions and scope

The process is the one-dimensional, two-velocity continuous-time run-and-tumble process with generator
\[
(\mathcal Lf)_\pm(x)=\pm v\,\partial_x f_\pm(x)+\lambda(x)(f_\mp(x)-f_\pm(x)).
\]
Here \(L,v\) are fixed positive real numbers and \(\lambda\) ranges over nonnegative continuous functions on the **closed** spatial interval. A trajectory starts at the left endpoint pointing *inward*, and that initial contact does **not** cause immediate absorption. Equivalently, the initial law is the inward-pointing limit of particles started at \(x\downarrow0\). Thereafter the outward-pointing boundary states \((0,-v)\) and \((L,+v)\) are absorbing; no specular reflection, diffusive noise, waiting at boundaries, or orientation-dependent rate is assumed. The rate is an actual velocity-reversal rate; in conventions where a 'tumbling event' redraws the direction uniformly, the reversal rate is half the event rate.

## Proof

For \(x\in[0,L]\), let \(h_\pm(x)\) be the probability of eventually exiting to the right starting at position \(x\) and direction \(\pm\). Their backward equations, with the outgoing-boundary conditions, are
\[
 v h_+'+\lambda(h_- -h_+)=0,\qquad
 -v h_-'+\lambda(h_+ -h_-)=0,\qquad
 h_-(0)=0,\quad h_+(L)=1.
\]
Subtracting the derivative relations gives \((h_+-h_-)'=0\), so \(h_+-h_-=p\), a constant equal to \(h_+(0)\). Thus \(h_-'=p\lambda/v\) and \(h_-(L)=pK\). The right condition becomes \(1=p(1+K)\), establishing \(p=1/(1+K)\).

Now let \(m_\pm(x)\) be the expected time to first *subsequent* absorption from those states. The backward equations and outgoing-boundary data are
\[
 v m_+'+\lambda(m_- -m_+)=-1,\qquad
 -v m_-'+\lambda(m_+ -m_-)=-1,\qquad
 m_-(0)=0,\quad m_+(L)=0.
\]
With \(d=m_+-m_-\), the derivative formulas yield \(d'(x)=-2/v\), and hence \(d(x)=\tau-2x/v\). The second equation gives \(m_-'=(1+\lambda d)/v\). Integration from \(0\) to \(L\) then gives
\[
 m_-(L)=\frac L v+K\tau-\frac{2B}{v},
 \qquad 0=m_+(L)=m_-(L)+\tau-\frac{2L}{v}.
\]
Therefore \(\tau(1+K)=(L+2B)/v\), proving the second identity. The backward solutions are the unique bounded solutions because, from each interior state, the probability of traveling straight to its facing endpoint without another reversal is at least \(e^{-K}>0\), and the waiting time until that event or exit is at most \(L/v\). A geometric domination argument gives finite mean exit time and validates the backward characterization.

If \(K=0\), continuity and nonnegativity force \(\lambda\equiv0\); thus \((p,\tau)=(1,L/v)\). For \(K>0\), introduce the rate centroid
\[
 \mu=\frac{\int_0^L x\lambda(x)\,dx}{\int_0^L\lambda(x)\,dx}=\frac BK.
\]
Because \(\lambda\ge0\) is continuous and not identically zero, it has positive mass in the open interval and \(0<\mu<L\). The exact formulas become
\[
 \tau=\frac{pL+2(1-p)\mu}{v},\qquad p=\frac{1}{1+K},
\]
which gives \(pL/v<\tau<(2-p)L/v\) with strict bounds.

Conversely, fix \(0<p<1\) and a time strictly between these bounds. The required centroid is
\[
 \mu=\frac{v\tau-pL}{2(1-p)}\in(0,L),\qquad K=\frac{1-p}{p}.
\]
The smooth exponential family
\[
 \lambda_\beta(x)=\frac{vK\,e^{\beta x/L}}{L\int_0^1e^{\beta s}\,ds},\qquad \beta\in\mathbb R,
\]
has total spatial rate integral \(vK\). Its normalized centroid varies continuously and strictly increasingly from \(0\) to \(L\), because differentiating the exponential tilt's mean with respect to \(\beta\) yields \(L\) times its strictly positive variance on \([0,1]\). Hence there exists a unique \(\beta\) realizing any prescribed \(\mu\). The endpoint bounds are approached as \(\beta\to-\infty\) and \(\beta\to+\infty\), but no continuous nonzero rate attains them.

Finally \(p\) identifies \(K=(1-p)/p\), and \(\tau\) then identifies \(B=(v\tau/p-L)/2\). Nevertheless, for any fixed exponential profile \(\lambda_\beta\), the perturbed profiles
\[
\widetilde\lambda_\varepsilon(x)=\lambda_\beta(x)+\varepsilon\cos(2\pi x/L)
\]
remain strictly positive and smooth for sufficiently small nonzero real \(\varepsilon\). The cosine has both zero zeroth moment and zero first moment on \([0,L]\), so all these distinct profiles produce the same observed pair \((p,\tau)\). Thus the inverse ambiguity is infinite even among strictly positive smooth rates.

## Verification

The claimed identities follow from the coupled backward equations and their correct outgoing-state boundary conditions. The supplied `check_simulation.py` independently simulates event-driven trajectories using integrated spatial hazard and a fixed random seed, avoiding a discretized approximation to the stochastic dynamics. For \(L=1.7\), \(v=1.4\), \(K=2.2\), and four positive profiles (uniform, exponentially increasing, exponentially decreasing, and sinusoidally modulated), twelve thousand simulated trajectories per profile agree with the exact splitting probability \(p=0.3125\) and exact mean-time predictions to statistical precision. The computational check is supporting evidence; it is not an infinite-dimensional proof.

## Relationship to prior work

Angelani, Di Leonardo and Paoluzzi (2014; lawful arXiv manuscript 1506.08046) give a general one-dimensional mean first-passage method for position-dependent motility and reversal rates, **with reflecting/absorbing endpoints**. That boundary problem has a different stopping event: return to the left endpoint is not absorption, and it does not yield our joint two-exit inverse-feasible region. Angelani's 2015 telegrapher treatment extends partial reflection at endpoints for a homogeneous bulk rate. Malakar et al. (2017 preprint; published 2018) explicitly compute exit probabilities and mean exit times for a *spatially homogeneous* reversal rate, including Brownian diffusion. Angelani (2023) treats general boundary kinetics, again assuming fixed bulk reversal rate. These papers supply the physical context and parts of the backward-equation technique but do not state the sharp two-observable region for **arbitrary heterogeneous** rate profiles. A related sharp mean-time envelope under **equiprobable initial directions at an interior launch point** concerns a different initial-state ensemble and only one observable; it does not imply the injected-state joint probability–time classification here.

## Limitations

This result covers a single noninteracting particle with fixed speed and equal position-dependent reversal rates for both velocity states. It does not cover finite tumbling durations, orientational asymmetry, Brownian diffusion, partially reflecting endpoints, or time-dependent rate profiles. The observational nonidentifiability concerns only the two global observables \((p,\tau)\), not the full exit-time distribution or data from multiple launch points. A related 2019 work on variable *speed* in partially absorbing domains was accessible only by abstract; its entire full text could not be inspected, leaving a limited literature-priority risk rather than direct evidence of coverage.

## References

1. L. Angelani, R. Di Leonardo, and M. Paoluzzi, “First-passage time of run-and-tumble particles,” *Eur. Phys. J. E* **37**, 59 (2014), published 2014-07-15. https://doi.org/10.1140/epje/i2014-14059-4 ; lawful manuscript https://arxiv.org/abs/1506.08046 (posted 2015-06-26).
2. L. Angelani, “Run-and-tumble particles, telegrapher’s equation and absorption problems with partially reflecting boundaries,” *J. Phys. A* **48**, 495003 (2015). https://arxiv.org/abs/1601.04845
3. K. Malakar et al., “Steady state, relaxation and first-passage properties of a run-and-tumble particle in one-dimension,” *J. Stat. Mech.* 043215 (2018); https://arxiv.org/abs/1711.08474 (first posted 2017-11-22).
4. L. Angelani, “One-dimensional run-and-tumble motions with generic boundary conditions,” *J. Phys. A* **56**, 455003 (2023). https://doi.org/10.1088/1751-8121/ad009e ; open text https://iris.cnr.it/handle/20.500.14243/450937.
5. L. Angelani and R. Garra, “Run-and-tumble motion in one dimension with space-dependent speed,” *Phys. Rev. E* **100**, 052147 (2019). https://doi.org/10.1103/PhysRevE.100.052147.
6. P. Singh, S. Sabhapandit, and A. Kundu, “Run-and-Tumble particle in inhomogeneous media in one dimension,” *J. Stat. Mech.* 2020 (2020). https://arxiv.org/abs/2004.11041.
