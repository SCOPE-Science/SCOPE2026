# Exact reversal of a Braess locking penalty on a four-oscillator cycle

## Finding
Consider four sinusoidally coupled phase oscillators whose path edges have unit weight and whose closing edge has adjustable weight \(a\geq0\). The natural frequencies are \((-1,0,0,1)\). Write \(K_c(a)\) for the infimum of the positive global coupling strengths admitting a phase-locked equilibrium that is **linearly asymptotically stable modulo common phase shifts**. Then, for every \(a\geq0\),

\[
K_c(a)=\begin{cases}
\dfrac{1}{1-a},&0\leq a\leq\dfrac19,\\
\dfrac{3\sqrt{3a}}{(1+3a)^{3/2}},&a\geq\dfrac19.
\end{cases}
\]

This continuous function is strictly increasing on \([0,1/6]\), strictly decreasing on \([1/6,\infty)\), and reaches \(K_c(1/6)=2/\sqrt3\). In particular \(K_c(0)=1\), \(K_c'(0)=1\), whereas \(K_c(1)=3\sqrt3/8<1\): the adverse infinitesimal effect of the closing edge reverses at finite weight. There is a unique \(a_*>1/6\) with \(K_c(a_*)=1\), given by the root in \((1/6,\infty)\) of \((1+3a)^3=27a\), approximately \(a_*=0.408893865635226\). Accordingly \(K_c(a)>K_c(0)\) precisely when \(0<a<a_*\), and \(K_c(a)<K_c(0)\) precisely when \(a>a_*\).

## Assumptions and scope
For \(i\in\{1,2,3,4\}\), phases \(\theta_i\in\mathbb T=\mathbb R/(2\pi\mathbb Z)\) evolve by

\[
\dot\theta_i=\omega_i+K\sum_{j=1}^4w_{ij}\sin(\theta_j-\theta_i),\qquad
\omega=(-1,0,0,1),\quad K>0,
\]

where \(w_{12}=w_{23}=w_{34}=1\), \(w_{14}=a\geq0\), and all other undirected weights vanish. A phase-locked equilibrium is an equilibrium of this vector field; it must have zero common angular velocity because the mean natural frequency is zero. Linear asymptotic stability **modulo global rotation** means the Jacobian has a single zero eigenvalue along \((1,1,1,1)\) and its other three eigenvalues are strictly negative. No dynamical claim is made at a nonhyperbolic threshold equilibrium.

## Proof
Put \(u_j=\theta_{j+1}-\theta_j\) for \(j=1,2,3\). At equilibrium, the two interior equations give \(\sin u_1=\sin u_2=\sin u_3=s\). The first endpoint equation becomes

\[
1=K\left(s+a\sin(u_1+u_2+u_3)\right).\tag{1}
\]

The negative Jacobian, divided by \(K\), has quadratic form on a variation \(v\in\mathbb R^4\)

\[
Q(v)=\sum_{j=1}^3\cos u_j(v_{j+1}-v_j)^2
+a\cos(u_1+u_2+u_3)(v_4-v_1)^2.\tag{2}
\]

If \(|s|=1\), every path cosine vanishes and the cosine of the sum also vanishes; thus the Jacobian is zero and cannot be strictly stable. Otherwise write \(t=\arcsin s\in(-\pi/2,\pi/2)\), \(c=\cos t>0\). Each \(u_j\) is, modulo \(2\pi\), either \(t\) or \(\pi-t\). We now exclude all choices having a flipped angle \(\pi-t\), whose path cosine is \(-c\).

If at least two path cosines are negative, choose a vector with \(v_1=v_4=0\) and increments supported on two negative links: \(v=(0,1,0,0)\) for links 1 and 2, \(v=(0,0,1,0)\) for links 2 and 3, or \(v=(0,1,1,0)\) for links 1 and 3. Its closing-edge contribution vanishes and \(Q(v)=-2c<0\). If only link 2 is negative, take \(v=(0,1,-1,0)\); its closing contribution vanishes and \(Q(v)=-2c\). If only link 1 or only link 3 is negative, then \(u_1+u_2+u_3\equiv\pi+t\), hence the closing cosine is also \(-c\). Taking \(v=(0,1,1,1)\) or \(v=(0,0,0,1)\), respectively, gives \(Q(v)=-(1+a)c<0\). Thus every strictly stable equilibrium must have \(u_1=u_2=u_3=t\) modulo \(2\pi\), with \(|t|<\pi/2\).

For these equal increments, equation (1) reads

\[
\frac1K=f_a(t):=\sin t+a\sin3t,
\]

and the quadratic form, writing \(d_j=v_{j+1}-v_j\), is

\[
Q(v)=c\sum_{j=1}^3d_j^2+a\cos3t\left(\sum_{j=1}^3d_j\right)^2.
\]

The three increments form arbitrary coordinates on the phase quotient, so strict positivity holds exactly when \(c>0\) and \(c+3a\cos3t=f_a'(t)>0\). Set \(s=\sin t\in(-1,1)\). The triple-angle identity gives

\[
f_a(t)=F_a(s):=(1+3a)s-4as^3,
\qquad \frac{dF_a}{ds}=1+3a-12as^2.\tag{3}
\]

For negative \(s=-r\), where \(0<r\leq1\), \(f_a(t)=-r-a\sin(3\arcsin r)\leq a\), while \(F_a(1/2)=1/2+a\). Hence a global maximizer occurs at positive \(s\). If \(0\leq a\leq1/9\), equation (3) is increasing on \(0\leq s<1\) and its supremum is \(F_a(1)=1-a\). If \(a>1/9\), the unique positive maximum is attained at

\[
s_*(a)=\sqrt{\frac{1+3a}{12a}}<1,
\qquad F_a(s_*)=\frac{(1+3a)^{3/2}}{3\sqrt{3a}}.\tag{4}
\]

Every strictly stable equilibrium has \(1/K=F_a(s)\) and therefore \(K\geq1/\sup F_a\). Conversely, for each \(K>1/\sup F_a\), the intermediate value theorem supplies a solution \(s\in(0,s_*)\) (using \(s_*=1\) in the first regime) of \(F_a(s)=1/K\). Equation (3) has strictly positive derivative there; thus the corresponding equal-increment equilibrium is strictly stable. This proves the formula for the infimum \(K_c(a)\), including at \(a=1/9\).

On \(a>1/9\), logarithmic differentiation yields

\[
\frac{d}{da}\log K_c(a)=\frac{1-6a}{2a(1+3a)}.
\]

On \(0\leq a\leq1/9\), \(K_c(a)=(1-a)^{-1}\) is increasing. The derivative formula therefore gives the unique maximum at \(a=1/6\) and strict decrease afterward. Substitution shows \(K_c(1)=3\sqrt3/8<1\) and \(K_c(a)\to0\) as \(a\to\infty\), proving the unique finite-weight crossing. The stated equation for that crossing follows by cubing the second formula for \(K_c\). Finally, differentiation of the first formula at zero gives \(K_c'(0)=1\).

## Verification
Run `python3 verify.py` using Python 3.9 or later; it uses only the standard library. The script checks rational triple-angle identities, compares the derived maximum to dense scalar sampling at fourteen weights, tests explicit unstable directions for every flipped phase pattern at twenty-five weight/sine combinations, constructs strictly stable phase-locked states above threshold by bisection, and checks the distinguished thresholds, monotonicity and crossing. The script reports 526 passing finite assertions. These computations do not prove the continuous-parameter or all-equilibrium statements; those follow from the analytic arguments above.

## Relationship to prior work
Arches, Fleurantin, Holzer, Sood and Uddin (2026, arXiv:2608.03594v1) derive a general first-order sensitivity formula for adding an edge to a Kuramoto network and demonstrate that this local signal is not always predictive of fully adding the edge. The present calculation makes that discrepancy exact in a specified four-vertex graph and supplies its entire edge-weight threshold curve and reversal weight. Their examples and formula are prior work, not claimed here. At the open-path threshold, the transverse Hessian has three zero eigenvalues, so a generic simple-fold perturbation theorem cannot simply be applied to this example; its derivative is derived directly from the exact formula.

Ottino-Löffler and Strogatz (2016, arXiv:1610.00296; *Physical Review E* 94, 062203) compare locking thresholds of chains and rings and give an explicit four-vertex counterexample with cumulative frequency vector \((1,-1,-1)\). The present vector has equal cumulative path flows \((-1,-1,-1)\), and the result here determines the continuous closing-edge-weight law, including reversal back to a beneficial edge. Manik, Timme and Witthaut (2016, arXiv:1611.09825) develop cycle-flow and stability methods and give a distinct Braess-type ring example. Their network identities and general stability framework are acknowledged; the specific sharp curve is not asserted to be absent from every possible older treatment.

## Limitations
The finding determines the **existence threshold for strict transverse linear stability**, not the basin of attraction of the locked state, stability exactly at the nonhyperbolic endpoint, synchronization from arbitrary initial conditions, or a result for unequal path weights or different natural-frequency patterns. The scalar triple-angle mechanism is special to this symmetric injection and three-edge path. The uncoupled path is multiply marginal at its threshold, so the derivative \(K_c'(0)=1\) is not asserted to follow from a simple-fold sensitivity theorem. Although inspected sources did not display the exact threshold curve, an equivalent result or a routine specialization of earlier general cycle-flow treatments remains a literature-priority risk. No independent scientific validation has been performed.

## References
1. Justin Arches, Emmanuel Fleurantin, Matt Holzer, Siddhant Sood, Shakeeb Uddin, *Predicting the occurrence of Braess paradox in the synchronization threshold of coupled oscillator systems*, arXiv:2608.03594v1, first submitted 2026-08-04. https://arxiv.org/abs/2608.03594
2. Bertrand Ottino-Löffler and Steven H. Strogatz, *Comparing the locking threshold for rings and chains of oscillators*, *Physical Review E* 94, 062203 (2016), arXiv:1610.00296. https://doi.org/10.1103/PhysRevE.94.062203
3. Debsankha Manik, Marc Timme, Dirk Witthaut, *Cycle flows and multistability in oscillatory networks: an overview*, arXiv:1611.09825v2 (2016). https://arxiv.org/abs/1611.09825
