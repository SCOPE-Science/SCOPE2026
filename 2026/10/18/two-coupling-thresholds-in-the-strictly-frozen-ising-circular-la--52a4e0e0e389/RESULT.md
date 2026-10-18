# Two coupling thresholds in the strictly frozen Ising circular ladder

## Finding
For a ferromagnetic two-leg periodic Ising ladder, strengthening the rung coupling produces **two discontinuities in the number of strictly one-spin-flip-blocked states**: an arbitrarily weak nonzero rung coupling activates exponentially many frozen configurations, and a rung coupling stronger than twice the leg coupling activates a larger exponential family. This concerns the landscape of strictly absorbing states, not an equilibrium thermal phase transition.

For every \(n\ge3\), define \(q=|K|\) and the polynomial
\[
S_n(z)=2+\sum_{\substack{2\le k\le\lfloor n/2\rfloor\\k\text{ even}}}
\frac{2n}{k}\binom{n-k-1}{k-1}z^k.
\]
A configuration has first-leg domain-wall count \(d\) and unsatisfied-rung count \(u\). For \(K\ne0\), an unsatisfied rung has \(\sigma_{1,i}\sigma_{2,i}\ne\operatorname{sgn}(K)\); at \(K=0\), define it by unequal spins. The exact absorbing-state polynomial \(F_{n,J,K}(z,w)=\sum_{\text{blocked states}}z^d w^u\) is
\[
F_{n,J,K}(z,w)=
\begin{cases}
2+2w^n,&q=0,\\
S_n(z)+2w^n,&0<q<2J,\\
S_n(z),&q=2J,\\
(1+z)^n+(1-z)^n,&q>2J.
\end{cases}
\]
In particular, \(S_n(1)=\varphi^n+(-\varphi^{-1})^n+2\cos(n\pi/3)\), with \(\varphi=(1+\sqrt5)/2\). The infinite-volume complexity per **spin** is therefore
\[
\lim_{n\to\infty}\frac1{2n}\log F_{n,J,K}(1,1)=
\begin{cases}
0,&q=0,\\
\frac12\log\varphi,&0<q\le2J,\\
\frac12\log2,&q>2J.
\end{cases}
\]
For uniformly sampled frozen configurations the first-leg domain-wall fraction converges in probability to \(0\), \((5-\sqrt5)/10\), or \(1/2\), respectively in these regimes.

## Assumptions and scope
There are exactly two labeled spin rows, indexed by \(r\in\{1,2\}\), and \(n\ge3\) labeled rungs, indexed cyclically. Every \(\sigma_{r,i}\in\{-1,1\}\). The Hamiltonian, including each of the two horizontal bonds per rung exactly once, is
\[
H(\sigma)=-J\sum_{r=1}^{2}\sum_{i=1}^{n}\sigma_{r,i}\sigma_{r,i+1}-K\sum_{i=1}^{n}\sigma_{1,i}\sigma_{2,i},
\qquad J>0,\quad K\in\mathbb R.
\]
No magnetic field is present. Zero-temperature dynamics allows an energy-lowering or energy-neutral single-spin flip whenever its rate is positive. A configuration is called *strictly absorbing* exactly when **each** individual flip would strictly increase \(H\). At equality of a local field to zero the state is not counted. The classification does not describe how often particular states are reached from a quench.

## Proof
**Local-field reduction.** Flipping \(\sigma_{r,i}\) changes the energy by
\[
\Delta_{r,i}H=2\sigma_{r,i}\bigl[J(\sigma_{r,i-1}+\sigma_{r,i+1})+K\sigma_{3-r,i}\bigr].
\]
The transformation \(\sigma_{2,i}\mapsto-\sigma_{2,i}\) conjugates the model with negative \(K\) to the model with positive \(q=|K|\), preserving every flip energy. Hence it suffices to treat \(K=q\ge0\).

When \(q=0\), each isolated leg must itself be uniformly magnetized: at any nonconstant binary cyclic word there is a spin with no equal horizontal neighbor or a domain-boundary spin with zero horizontal local field. Thus there are four strictly absorbing pairs of constant legs, two parallel and two antiparallel, giving \(2+2w^n\).

When \(q>0\) and some rung is antiparallel, each of its spins has an opposing rung neighbor. Strict stability forces **both** horizontal neighbors of each spin to agree with it, because one opposing horizontal neighbor would leave local field at most \(-q\). This forces the adjacent rungs to be antiparallel in the same orientation. Propagation around the ring leaves only the two states with opposite, constant legs. Their local fields are strictly favorable exactly when \(2J-q>0\), so they contribute \(2w^n\) for \(0<q<2J\), and nothing at or above \(q=2J\).

In every other blocked configuration all rungs align. Write their common spins as \(s_i\). The strict local-field requirement reduces to
\[
q+J(s_is_{i-1}+s_is_{i+1})>0\quad\text{for each }i.
\]
For \(0<q\le2J\), this excludes precisely length-one cyclic runs (the case \(q=2J\) is excluded because its boundary flips are energy-neutral). For \(q>2J\) it imposes no restriction. This is a necessary-and-sufficient classification; in particular it excludes no other possibilities.

**Exact wall counts.** A nonconstant allowed cyclic word has an even number \(k\) of domain walls, with \(2\le k\le\lfloor n/2\rfloor\), and \(k\) runs each of length at least two. Choose a labeled starting site and one of two starting signs. There are \(\binom{n-k-1}{k-1}\) ordered compositions of \(n\) into \(k\) parts at least two. Every cyclic word is thereby represented exactly \(k\) times, giving \(\frac{2n}{k}\binom{n-k-1}{k-1}\). The two uniform words contribute two. At \(q>2J\), choose any even-size set of \(k\) domain walls among the \(n\) horizontal bonds and one of two signs, giving \(2\binom nk\); its generating polynomial is \((1+z)^n+(1-z)^n\). The two uniform antiparallel leg configurations account for the additional \(2w^n\) at intermediate coupling.

**Asymptotic complexity and walls.** In the ordered pair-state basis \((00,01,10,11)\), the allowed no-singleton transfer matrix, with \(z\) for a new domain wall, is
\[
M(z)=\begin{pmatrix}1&z&0&0\\0&0&0&1\\1&0&0&0\\0&0&z&1\end{pmatrix},
\qquad S_n(z)=\operatorname{tr}(M(z)^n).
\]
Its characteristic polynomial is \((t^2-t)^2-z^2\). For real \(z>0\), the spectral radius is the unique positive Perron root \(\lambda(z)=(1+\sqrt{1+4z})/2\); the other three eigenvalues have strictly smaller modulus. At \(z=1\), the other eigenvalues are \(-\varphi^{-1}\) and \(e^{\pm i\pi/3}\), proving the stated finite-size cosine identity. Consequently the per-rung logarithmic generating function converges to \(\log\lambda(z)\) at intermediate coupling, and to \(\log(1+z)\) at strong coupling. The wall fractions of the associated uniform counting measures concentrate at
\[
\left.z\frac{d}{dz}\log\lambda(z)\right|_{z=1}
=\frac{1}{\varphi\sqrt5}=\frac{5-\sqrt5}{10},
\qquad
\left.z\frac{d}{dz}\log(1+z)\right|_{z=1}=\frac12,
\]
by the standard exponential-moment argument, since the limiting logarithmic generating functions are differentiable near \(z=1\). At zero coupling every blocked first leg is uniform, so its wall fraction is zero. Division by the \(2n\) spins yields the complexity per spin.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 and its standard library. It enumerates all \(2^{2n}\) spin pairs for each \(3\le n\le8\) at nine coupling values including both signs, zero, and the resonance \(q=2J\) (54 complete cases). Independently it multiplies a polynomial transfer matrix and checks all coefficients of \(S_n(z)\) for \(3\le n\le30\) (28 exact comparisons). All these checks passed. The all-size conclusion follows from the preceding symbolic proof, not from the enumeration.

## Relationship to prior work
Shukla (2005) explicitly describes parallel rungs with no length-one domains as a zero-temperature Glauber frozen pattern on a uniform-coupling ladder. That known branch is not claimed as new. The present statement treats the complete *strictly absorbing set*, includes the antiparallel constant-leg states, and gives a coupling-dependent finite-size generating polynomial and two exact exponential-complexity thresholds. De Smedt, Godrèche, and Luck (2002) study energy-counting and blocked states for kinetically constrained *single chains*, not this anisotropic prism; Waclaw and Burda (2008) approximate a mean metastable complexity for *random Gaussian* couplings, including ladders, not this fixed ferromagnetic coupling family. A separate facilitated-kinetic model on a prism has different allowed moves and does not imply the Ising local-field thresholds.

## Limitations
These are exact strict one-spin-flip local energy minima for finite periodic two-leg ladders, and their uniform *a priori* counts. No assertion is made about low-temperature escape times, attraction-basin probabilities, stationary Gibbs phase transitions, or wider ladders. At the special couplings \(q=0\) and \(q=2J\), configurations with neutral flips are excluded by definition. Although the primary sources examined do not cover the complete anisotropic phase diagram, equivalent results under different descriptions may exist, and no database search proves global uniqueness.

## References
1. G. De Smedt, C. Godrèche, and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems*, arXiv:cond-mat/0202465 (first posted 2002-02-26). https://arxiv.org/abs/cond-mat/0202465
2. P. Shukla, *Voter Dynamics on an Ising Ladder: Coarsening and Persistence*, arXiv:cond-mat/0501754 (first posted 2005-01-31), especially Introduction and its zero-temperature Glauber discussion. https://arxiv.org/abs/cond-mat/0501754
3. B. Waclaw and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224 (first posted 2008-01-08), especially Section VII on ladders. https://arxiv.org/abs/0801.1224
