# A sharp fourth-moment frontier for randomly sampled double-integrator feedback

## Finding
Consider the double integrator \(\dot q=v\), \(\dot v=u\) under zero-order-hold state feedback \(u(t)=-k_p q(t_j)-k_d v(t_j)\) for \(t_j\le t<t_{j+1}\). Sampling increments \(H_j=t_{j+1}-t_j>0\) are independent and identically distributed, independent of the initial state. We consider *exponential mean-square stability in the sampling index*: there are \(C<\infty\) and \(0<r<1\) such that \(\mathbb E\| (q(t_j),v(t_j))\|^2\le Cr^j\|(q(0),v(0))\|^2\) for every deterministic initial state and every \(j\ge0\).

For any fixed \(k_p,k_d>0\), among sampling laws with the same first three raw moments and finite fourth moment, increasing the fourth raw moment **cannot decrease** the covariance transition operator's spectral radius.

For the particular gains \(k_p=4/3\), \(k_d=1\), and every positive sampling law satisfying
\[
\mathbb EH=\frac9{10},\qquad \mathbb EH^2=\frac{113}{100},\qquad \mathbb EH^3=\frac{1593}{1000},
\]
we obtain the *sharp, distribution-independent* classification
\[
\boxed{\text{exponential mean-square sampled-index stability}\quad\Longleftrightarrow\quad \mathbb EH^4<\frac{642421}{270000}.}
\]
At equality there is a unit covariance eigenvalue, so exponential mean-square stability fails; strictly above the threshold the second moment grows for a suitable initial state.

Two strictly positive five-point laws with identical first three moments lie on different sides. On the common support \(\{1/10,1/2,9/10,13/10,17/10\}\), put probabilities respectively
\[
\mu_-=(7,12,2,12,7)/40,\qquad \mu_+=(9,4,14,4,9)/40.
\]
Then \(\mathbb E_{\mu_-}H^4=118501/50000\) gives stability, whereas \(\mathbb E_{\mu_+}H^4=120037/50000\) gives instability. Thus the mean, variance and skewness do not determine mean-square stability even when support is fixed.

## Assumptions and scope
The continuous-time plant, gains, zero-order hold, i.i.d. positive intervals, and finite fourth moment are as above. No bounded-support hypothesis is needed for the universal moment ordering or the sharp classification. The stability conclusion concerns the discrete sequence of states **at sampling times**, measured per sampling step, rather than decay per unit physical time. This does not assert an intersample bound for unbounded intervals or almost-sure stability. The two example distributions have strictly positive masses at all five stated support points.

## Proof
**Sampled map.** Integrating the held acceleration exactly gives
\[
\begin{pmatrix}q(t_{j+1})\\ v(t_{j+1})\end{pmatrix}=A(H_j)\begin{pmatrix}q(t_j)\\v(t_j)\end{pmatrix},\quad
A(h)=\begin{pmatrix}1-k_ph^2/2&h-k_dh^2/2\\-k_ph&1-k_dh\end{pmatrix}.
\]
Define the covariance map \(\mathcal T_\mu(X)=\mathbb E_\mu[A(H)XA(H)^\mathsf T]\) on real symmetric \(2\times2\) matrices. It is positive on the cone of positive semidefinite matrices. For i.i.d. sampling the second moment evolves through \(\mathcal T_\mu^j\). Exponential mean-square sampled-index stability for all initial conditions is equivalent to \(\rho(\mathcal T_\mu)<1\): one direction follows from finite-dimensional spectral theory; the other follows because rank-one positive semidefinite matrices span the symmetric matrices, and positive inputs include all deterministic initial covariances.

**Universal fourth-moment ordering.** Write \(e_1=(1,0)^\mathsf T\) and \(g=(k_p,k_d)^\mathsf T\). The coefficient of \(h^4\) in \(A(h)XA(h)^\mathsf T\) is exactly \(e_1(g^\mathsf TXg)e_1^\mathsf T/4\). Thus for laws \(\mu,\nu\) with equal moments of orders \(0,1,2,3\),
\[
\mathcal T_\nu(X)-\mathcal T_\mu(X)=\frac{\mathbb E_\nu H^4-\mathbb E_\mu H^4}{4}\ e_1(g^\mathsf TXg)e_1^\mathsf T.
\]
For \(X\succeq0\) this difference is positive semidefinite whenever the fourth-moment difference is nonnegative. Cone order is preserved under composition of positive linear maps; hence \(0\le\mathcal T_\mu^j\le\mathcal T_\nu^j\) on positive semidefinite inputs. A cone-adapted norm, followed by Gelfand's formula, implies \(\rho(\mathcal T_\mu)\le\rho(\mathcal T_\nu)\).

**Exact covariance matrix.** Use coordinates \((x,y,z)\) for \(X=\left(\begin{smallmatrix}x&y\\y&z\end{smallmatrix}\right)\). With the stated gains and first three moments, direct expansion yields
\[
S(m)=\begin{pmatrix}
4m/9-38/75&2m/3-727/500&m/4-463/1000\\
27/125&-9/250&3/2000\\
452/225&46/75&33/100
\end{pmatrix},\qquad m=\mathbb E H^4.
\]
It follows by exact determinant expansion that
\[
\det(I-S(m))=\frac{24}{25}\left(\frac{642421}{270000}-m\right).
\]

**Stable anchor.** At \(m_-=118501/50000\), the distribution \(\mu_-\) above has the specified lower moments. The following positive definite rational matrix is a *strict stochastic Lyapunov certificate*:
\[
P=\begin{pmatrix}
8175625/25156&3909625/100624\\3909625/100624&25955165/402496
\end{pmatrix}.
\]
Exact substitution gives \(P-\mathbb E_{\mu_-}[A(H)^\mathsf TPA(H)]=I_2\), and \(P_{11}>0\), \(\det P=2590980634375/133226176>0\). Consequently \(\rho(S(m_-))<1\). The upper law has \(m_+=120037/50000\), which exceeds \(642421/270000\); indeed \(\det(I-S(m_+))=-14447/703125<0\), implying an eigenvalue strictly greater than one.

**All feasible fourth moments.** For every feasible \(m\le m_-\), cone ordering gives \(\rho(S(m))\le\rho(S(m_-))<1\). Every \(m\in[m_-,m_+]\) is realized by a mixture of \(\mu_-\) and \(\mu_+\), with exactly the same first three moments. Along this continuous positive-operator segment, the spectral radius is a nonnegative real eigenvalue (Perron--Frobenius theory for proper cones). Starting from the stable anchor, it can reach one only where \(\det(I-S(m))=0\), namely at \(m_*=642421/270000\). This is a unique crossing because the determinant is a nonconstant affine function of \(m\); at the crossing, a unit eigenvalue precludes exponential stability. For every \(m>m_*\), \(\det(I-S(m))<0\), so the real cubic characteristic polynomial has an eigenvalue greater than one. In particular this applies to all feasible \(m\ge m_+\). This proves the stated if-and-only-if classification and the stable/unstable matched-moment pair.

## Verification
Run `python verify.py` from the directory containing the attached stand-alone script; SymPy is its only dependency. Its exact rational assertions reconstruct both sampling distributions' first four moments, the full covariance matrices, the determinant formula, the displayed positive-definite Lyapunov matrix and its residual, and the generic fourth-order rank-one identity. No finite search or floating-point output is used as the proof of the universal statement.

## Relationship to prior work
Random sampling and stochastic stability of networked control are classical. Montestruque and Antsaklis (2003) treat stochastic, variable-update networked systems, including a double-integrator example, via model-based network control stability conditions; their controller intersample model and stated analysis do not present the present zero-order-hold, fixed-moment order or explicit threshold. Their 2004 treatment develops time-varying transmission stability with iid and Markov cases. Li et al. (2013) study Markov-modulated sampling and delay with mode-dependent control, yielding LMI conditions; its full text does not state the rank-one moment-order law or this rational sharp fixed-lower-moment boundary. Agniel and Jury (1971) address randomly sampled stability at a more general level; the full article was not available for complete comparison. General covariance-lifting and Lyapunov facts are background, not asserted to be original.

## Limitations
The universal fourth-moment ordering is conditional on matching **all three** lower raw moments and uses the particular zero-order-hold double-integrator structure. The displayed sharp threshold is specific to the stated gains and lower-moment triple. No assertion is made for general correlated sampling, time-delay models, time-domain asymptotic stability, or general continuous plants. Full-text overlap with some early literature remains a residual originality risk; no independent audit has been conducted.

## References
- L. A. Montestruque and P. J. Antsaklis, “Stochastic Stability for Model-Based Networked Control Systems,” American Control Conference (2003), DOI: 10.1109/ACC.2003.1240481.
- L. A. Montestruque and P. J. Antsaklis, “Stability of Model-Based Networked Control Systems With Time-Varying Transmission Times,” *IEEE Transactions on Automatic Control* 49 (2004), DOI: 10.1109/TAC.2004.834107.
- Y. Li, Q. Zhang, S. Zhang and M. Cai, “Stabilization for Networked Control Systems with Random Sampling Periods,” *Journal of Applied Mathematics* (first published 2013-03-06), DOI: 10.1155/2013/252679.
- R. G. Agniel and E. I. Jury, “Almost Sure Boundedness of Randomly Sampled Systems,” *SIAM Journal on Control* (1971), DOI: 10.1137/0309027.
