# Exact revival thresholds and a logarithmic counting law for telegraph-noisy qubit channels

## Finding

Consider a stationary symmetric two-state telegraph process \(X_t\in\{-1,1\}\), switching from either state to the other at rate \(\lambda\ge0\). For \(\lambda=0\), take a fair, static initial sign. A qubit undergoes the random Hamiltonian \(H(t)=\tfrac v2 X_t\sigma_z\), where \(v>0\). Independently, it experiences isotropic depolarization at rate \(\kappa>0\), with depolarizing semigroup \(\mathcal D_t(\rho)=e^{-\kappa t}\rho+(1-e^{-\kappa t})\operatorname{Tr}(\rho)I/2\). Denote the ensemble-averaged channel by \(\Phi_t\).

**Theorem.** If \(0\le\lambda<v\), let
\[
\omega=\sqrt{v^2-\lambda^2},\quad \theta=\arctan(\lambda/\omega),\quad z_j=\frac{\theta+\pi/2+j\pi}{\omega},\quad t_j=\frac{(j+1)\pi}{\omega}\quad (j=0,1,\ldots).
\]
For each \(j\ge0\), define the exact critical depolarization rate
\[
\kappa_j=\max_{z_j<t<z_{j+1}}\frac{\log(1+2|f(t)|)}{t},\qquad f(t)=e^{-\lambda t}\left(\cos(\omega t)+\frac\lambda\omega\sin(\omega t)\right).
\]
The maximum is attained in the interior and the sequence \((\kappa_j)_{j\ge0}\) is strictly decreasing to zero. The channel loses the ability to preserve entanglement at exactly one time in \((0,z_0)\). Between consecutive zeros \(z_j,z_{j+1}\), it is **not** entanglement breaking on exactly one nonempty open interval if and only if \(\kappa<\kappa_j\); if \(\kappa\ge\kappa_j\), the channel is entanglement breaking throughout that lobe. All such revival intervals are eventually absent for any fixed \(\kappa>0\).

The thresholds have explicit two-sided bounds, valid also at \(\lambda=0\):
\[
\frac{\log(1+2e^{-\lambda t_j})}{t_j}\le\kappa_j\le
\frac{\log(1+2e^{-\lambda t_j})}{z_j}.
\]
Thus, for fixed \(0<\lambda<v\),
\[
\kappa_j\sim\frac{2e^{-\lambda(j+1)\pi/\omega}}{(j+1)\pi/\omega}.
\]
If \(N(\kappa)=\#\{j\ge0:\kappa<\kappa_j\}\) is the exact number of post-first-death entanglement-preserving revival intervals, then as \(\kappa\downarrow0\),
\[
\boxed{N(\kappa)=\frac\omega{\pi\lambda}W\!\left(\frac{2\lambda}{\kappa}\right)+O_{v,\lambda}(1)
=\frac\omega{\pi\lambda}\left[\log\!\frac{2\lambda}{\kappa}-\log\log\!\frac{2\lambda}{\kappa}\right]+O_{v,\lambda}(1),}
\]
where \(W\) is the principal Lambert function. At the static-noise endpoint \(\lambda=0\), the scaling changes discontinuously to
\[
\boxed{N(\kappa)=\frac{v\log3}{\pi\kappa}+O_v(1).}
\]
If \(\lambda\ge v\), the channel instead has a single transition from non-entanglement-breaking to permanently entanglement-breaking, and no revivals.

## Assumptions and scope

The two-state process is initialized in its stationary, fair distribution; switches are memoryless at the specified per-direction rate. Its integrated phase rotates a **single** qubit around a fixed axis. The independent isotropic depolarization acts on the same qubit, and the ensemble average is taken before testing the induced channel on arbitrary input–reference states. The question is whether \(\Phi_t\) is entanglement breaking, not whether one selected initial two-qubit state remains entangled. Times \(t\) are nonnegative, \(v>0\), \(\kappa>0\), and \(\lambda\ge0\). The asymptotics hold with \(v\) and \(\lambda\) fixed, so they are not claimed uniformly as \(\lambda\downarrow0\).

## Proof

**1. Telegraph coherence and Choi criterion.** Conditional characteristic functions \(u_\pm(t)=\mathbb E[e^{-iv\int_0^t X_sds}\mid X_0=\pm1]\) solve \(u_\pm'=\mp ivu_\pm+\lambda(u_\mp-u_\pm)\), with \(u_\pm(0)=1\). Their fair average \(f=(u_++u_-)/2\) solves
\[
f''+2\lambda f'+v^2f=0,\quad f(0)=1,\quad f'(0)=0.
\]
It is real. For \(\lambda<v\), solution gives the formula in the theorem. For \(\lambda=v\), \(f=e^{-\lambda t}(1+\lambda t)\); for \(\lambda>v\), setting \(\mu=\sqrt{\lambda^2-v^2}\) gives \(f=e^{-\lambda t}(\cosh\mu t+(\lambda/\mu)\sinh\mu t)\). In all cases the Pauli transfer multipliers of \(\Phi_t\) are
\[
(e^{-\kappa t}f(t),e^{-\kappa t}f(t),e^{-\kappa t}).
\]
The unital-qubit entanglement-breaking criterion (Ruskai, Theorem 4) states that the sum of their absolute values is at most one. Equivalently,
\[
\Phi_t\text{ is not entanglement breaking}\quad\Longleftrightarrow\quad |f(t)|>h_\kappa(t):=\frac{e^{\kappa t}-1}{2}.
\]
The least eigenvalue of the partially transposed normalized Choi state equals \([1-e^{-\kappa t}(1+2|f(t)|)]/4\), so equality belongs to the entanglement-breaking region.

**2. Zero structure and exact threshold hierarchy.** Suppose \(\lambda<v\). Writing \(f(t)=(v/\omega)e^{-\lambda t}\cos(\omega t-\theta)\) gives the stated zeros and the alternating-sign open lobes \(I_j=(z_j,z_{j+1})\). The derivative \(f'(t)=-(v^2/\omega)e^{-\lambda t}\sin(\omega t)\) shows that \(|f|\) has one maximum on \(I_j\), at \(t_j\), of value \(e^{-\lambda t_j}\). Before \(z_0\), \(f\) decreases strictly from one to zero, while \(h_\kappa\) increases strictly from zero, hence there is exactly one initial crossing.

For \(t\in I_j\),
\[
|f(t)|=(v/\omega)e^{-\lambda t}\sin\big(\omega(t-z_j)\big).
\]
Consequently, the second derivative of \(\log(|f|/h_\kappa)\) is
\[
-\omega^2\csc^2\big(\omega(t-z_j)\big)
+\left(\frac{\kappa}{2\sinh(\kappa t/2)}\right)^2
< -\omega^2+\frac1{t^2}<0,
\]
because \(t>z_0\ge\pi/(2\omega)>1/\omega\). The logarithmic ratio is strictly concave and tends to negative infinity at both ends of the lobe. Therefore its positive superlevel set is either empty or a single open interval. Since \(|f(t)|>h_\kappa(t)\) is equivalent to \(\kappa<t^{-1}\log(1+2|f(t)|)\), the nonempty case is exactly \(\kappa<\kappa_j\).

Let \(P=\pi/\omega\). For every \(t\in I_j\), \(t+P\in I_{j+1}\) and \(|f(t+P)|=e^{-\lambda P}|f(t)|\). Therefore
\[
\frac{\log(1+2|f(t+P)|)}{t+P}
<\frac{\log(1+2|f(t)|)}t.
\]
Evaluating this strict inequality at a maximizing point of the next lobe proves \(\kappa_{j+1}<\kappa_j\). Every threshold is positive and finite; the bounds below prove convergence to zero.

**3. Quantitative critical-rate bounds.** The maximum \(|f|=e^{-\lambda t_j}\) at \(t_j\) supplies the lower bound for \(\kappa_j\). Every \(t\in I_j\) obeys \(t\ge z_j\) and \(|f(t)|\le e^{-\lambda t_j}\), supplying the upper bound. Since \(t_j-z_j=(\pi/2-\theta)/\omega\) is independent of \(j\), the bounds yield
\[
\kappa_j=\frac{2e^{-\lambda t_j}}{t_j}\bigl(1+O_{v,\lambda}(j^{-1}+e^{-\lambda t_j})\bigr),\qquad 0<\lambda<v.
\]
For \(\lambda=0\), they instead yield \(\kappa_j=(\log3)/t_j+O_v(j^{-2})\).

**4. Counting.** Strict ordering gives exactly \(N(\kappa)=\#\{j:\kappa<\kappa_j\}\) revival intervals, a finite number at every positive \(\kappa\). Set \(n=j+1\) and \(t_j=n\pi/\omega\). The threshold bounds squeeze the transition index between solutions of \(\kappa=2e^{-\lambda n\pi/\omega}/(n\pi/\omega)\), up to a bounded index change: their multiplicative error is \(1+O(1/n)\), whereas adjacent thresholds have asymptotic ratio \(e^{-\lambda\pi/\omega}<1\). Rearrangement gives \(\lambda n\pi/\omega=W(2\lambda/\kappa)\). The standard real asymptotic \(W(x)=\log x-\log\log x+o(1)\) proves the claimed two-term counting law with bounded remainder. At \(\lambda=0\), the bounds squeeze the transition index between \((\log3)/(n\pi/v)\) and the same expression multiplied by \(1+O(1/n)\), giving \(N(\kappa)=v\log3/(\pi\kappa)+O_v(1)\).

**5. Overdamped and critically damped regions.** For \(\lambda>v\), direct differentiation gives \(f'(t)=-(v^2/\mu)e^{-\lambda t}\sinh(\mu t)<0\) for all \(t>0\), and \(f(t)>0\). At \(\lambda=v\), \(f'(t)=-v^2te^{-vt}<0\). In both cases \(f\) decreases to zero, while \(h_\kappa\) increases to infinity, so there is one crossing and no revival.

## Verification

The accompanying `verify.py` independently reconstructs telegraph characteristic functions by exponentiating their two-state generator; reconstructs the normalized Choi matrix and partial transpose from Pauli transfer multipliers; checks the exact critical-rate bracketing and strict ordering; and compares computed revival counts against the Lambert and static-noise limits. It also samples representative time lobes to check the predicted sign topology. Execute using Python with the versions specified in `requirements.txt`:

```sh
python verify.py
```

These checks are finite and numerical; the statements for all positive times, infinitely many lobes, and the vanishing-rate limits follow from the preceding proof, not enumeration.

## Relationship to prior work

Ruskai (2003) provides the unital-qubit entanglement-breaking criterion; this criterion is not claimed as new. Zhou, Lang and Joynt (2009/2010) analytically describe telegraph-driven two-qubit entanglement sudden death and revivals, including finite revival counts when relaxation is present. D'Arrigo and collaborators (2012) derive the characteristic oscillatory coherence factor and interpret telegraph-induced entanglement revivals. Shrikant, Srikanth and Banerjee (2018) develop non-Markovian dephasing/depolarizing channel constructions and focus on divisibility rather than these thresholds. The contribution assessed here is the exact strictly ordered depolarization thresholds **for every oscillation lobe** and the sharp Lambert/logarithmic-versus-inverse-rate asymptotic number of revival intervals under a separately specified isotropic depolarizer. It is not a claim to have discovered telegraph revivals, the elementary qubit Choi criterion, or the general qualitative finiteness of revivals under relaxation.

## Limitations

The theorem requires a fair stationary telegraph process, a single noise axis, an independent isotropic Markovian depolarizer, and exactly one qubit. A different definition of switching rate changes the numerical factors in the formulas. The two vanishing-noise regimes are not uniform in the joint limit \(\lambda,\kappa\downarrow0\). Counting complete revivals of all input–reference entanglement (via the entanglement-breaking property) is not equivalent to counting revivals for an arbitrary fixed nonmaximally entangled input. Nothing is asserted about thermal amplitude damping, multiple fluctuators, finite experimental observation windows, or experimental statistical power. Independent priority assessment of the precise threshold and counting law remains open.

## References

1. M. B. Ruskai, *Qubit Entanglement Breaking Channels*, arXiv:quant-ph/0302032 (first public version 2003-02-04), especially Theorem 4. https://arxiv.org/abs/quant-ph/0302032
2. D. Zhou, A. Lang and R. Joynt, *Disentanglement and decoherence from classical non-Markovian noise: Random telegraph noise*, arXiv:0912.3313 (first public version 2009-12-17), especially equation (37) and Sections V–VII. https://arxiv.org/abs/0912.3313
3. A. D'Arrigo, R. Lo Franco, G. Benenti, E. Paladino and G. Falci, *Hidden entanglement in the presence of random telegraph dephasing noise*, arXiv:1210.1122 (first public version 2012-10-03), especially equation (5) and Section 3. https://arxiv.org/abs/1210.1122
4. U. Shrikant, R. Srikanth and S. Banerjee, *Non-Markovian Dephasing and Depolarizing Channels*, arXiv:1805.11411 (2018), Sections II and VI. https://arxiv.org/abs/1805.11411
