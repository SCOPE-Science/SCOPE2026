# Scientific assessment

## Mathematical claim and domain

For fixed $a\in\mathbb R$, $\kappa>0$, the cubic center $\dot x=y$, $\dot y=-x+(a-\kappa x)y^2$ admits an exact original-time Hamiltonian conjugacy. On every energy $E>0$, the orbit is periodic. The large-energy minimal period obeys $T(E)\sqrt{\log E}\to2\pi$. Canonical position and momentum approach the unit harmonic orbit uniformly in normalized phase; the original coordinate instead converges in each finite $L^p$ to a square wave, and its physical-time occupation tends to the equal mixture at $-1$ and $+1$. All limits fix the parameters.

## Correctness — PASS

With $g(x)=\exp(\kappa x^2/2-ax)$, $q(x)=\int_0^x g(u)du$, $p=g(x)y$ and $V(x)=\int_0^x ug(u)^2du$, the invariant $H=p^2/2+V(x)=p^2/2+W(q)$ produces $\dot q=p$ and $\dot p=-W'(q)$ in the original physical time. The positive global integrating factor gives the required entire coordinate diffeomorphism and a coercive single-well potential. Its signed Gaussian tails yield $W(q)\sim q^2\log|q|$ and $W'(q)\sim2q\log|q|$. The exact $W''(q)=1+x(\kappa x-a)$ gives locally uniform, equi-Lipschitz convergence of the properly scaled force to $z$, whence the harmonic limit and the minimal-period constant. Inverting the Gaussian-tail coordinate away from the two harmonic zeros gives the square wave; global turning bounds prove the stated $L^p$ and occupation limits by domination. Algebraic and numerical checks support rather than establish these infinite limits.

## Originality — PASS, best of current knowledge

Appis and Llibre, *Global centers of a family of cubic systems* (2024), Theorem 4(a), proves qualitative global-center existence in this coefficient slice, which is credited and not treated as new. Villadelprat and Zhang, *The Period Function of Hamiltonian Systems with Separable Variables* (2019/2020), Theorem 5.1(b), proves that the period tends to zero when both stiffness limits are infinite; its complete preprint does not yield the stated leading logarithmic coefficient or inverse-observable occupation. Cima, Gasull and Mañosas, *Period Function for a Class of Hamiltonian Systems* (2000), Theorem C, assumes pure-power inverse-length derivatives and does not directly apply to the slowly varying factor in this transformed potential. Published mathematical records about two other cubic global centers were compared by their actual vector fields and asymptotic implications; neither covers this claim. An exact record of the finding itself was excluded from priority evidence. Residual risks include unindexed regular-variation and equivalent oscillator literature.

## Mathematical value — PASS

The full high-energy behavior of a natural globally periodic cubic family is a worthwhile dynamical question: its original-time angular frequency and time-occupation statistics are not determined by existence of a center. The result quantifies a distinctive singular mismatch between canonical harmonic shape and original-coordinate square-wave residence, with explicit constants and a complete fixed-parameter regime. It does not assert finite-energy monotonicity, a jump-layer profile, rate estimates or extension to arbitrary cubic centers.

## Primary references

- Appis & Llibre (2024), https://doi.org/10.1007/s00010-024-01051-7 (full open article, Theorem 4(a)).
- Villadelprat & Zhang (2019 preprint; 2020 journal), https://doi.org/10.1007/s10884-019-09759-w (full author preprint, Theorem 5.1 and proof).
- Cima, Gasull & Mañosas (2000), https://doi.org/10.1006/jdeq.2000.3912 (primary full text, Theorem C and proof).
- Buzzi, Carvalho & Gasull (2020 preprint), https://arxiv.org/abs/2008.02316 (abstract-level screening only).

## Scope and risk

The leading canonical period may also be accessible through more general regular-variation oscillator theory; the published priority comparison is best-of-knowledge, not an absolute novelty certificate. The original-coordinate claim is $L^p$ for finite $p$, not uniform convergence at the two jump phases. No Lean proof or external human attestation is claimed.
