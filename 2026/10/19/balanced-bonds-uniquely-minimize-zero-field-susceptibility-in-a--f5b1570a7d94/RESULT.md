# Balanced bonds uniquely minimize zero-field susceptibility in a ferromagnetic Ising ring

## Finding
Consider a periodic Ising chain with \(n\ge3\) spins, exactly \(m\) strong bonds and \(n-m\) weak bonds, where \(1\le m<n\). At every positive inverse temperature and for every pair of strictly positive, distinct ferromagnetic couplings, the dimensionless zero-field magnetic susceptibility is minimized **exactly** by the cyclic rotations of the balanced mechanical bond word
\[
 b_j=\left\lfloor\frac{(j+1)m}{n}\right\rfloor-\left\lfloor\frac{jm}{n}\right\rfloor,\qquad 0\le j<n.
\]
This is a global and strict statement over all \(\binom nm\) assignments of the two couplings to the labeled edges, with uniqueness understood modulo rotation. Thus the minimizing geometry is independent of temperature and of the strength ratio.

Here is an exact finite-size minimum. Set
\[
 x=\tanh(\beta J_{\rm strong}),\quad
 y=\tanh(\beta J_{\rm weak}),\quad
 q=x/y,\quad P=x^m y^{n-m},
\]
so that \(0<y<x<1\). For each \(1\le k<n\), write \(km=nr_k+s_k\), with \(0\le s_k<n\). With \(M=\sum_{j=0}^{n-1}\sigma_j\) and \(\mathcal S=\operatorname{Var}(M)/n\), the sharp minimum is
\[
 \boxed{\displaystyle
 \mathcal S_{\min}(n,m;x,y)=1+\frac{2}{n(1+P)}
 \sum_{k=1}^{n-1}y^k\left[(n-s_k)q^{r_k}+s_kq^{r_k+1}\right].}
\]
The physical susceptibility per spin, defined by differentiating magnetization with respect to a uniform energy-valued magnetic field, is \(\beta\mathcal S\); it has the same minimizers.

The phenomenon is hidden from the zero-field free energy: **every permutation of the bonds has exactly the same zero-field partition function**, although the field susceptibility generally changes.

For an equimolar sequence of even ring lengths \(n=2m\to\infty\), alternating bonds attain the minimum, with
\[
 \lim_{m\to\infty}\mathcal S_{\rm alt}
   =\frac{(1+x)(1+y)}{1-xy}.
\]
When instead the strong bonds form one block of length \(m\) and the weak bonds the complementary block,
\[
 \lim_{m\to\infty}\mathcal S_{\rm blocks}
  =\frac12\left(\frac{1+x}{1-x}+\frac{1+y}{1-y}\right),
\]
and the thermodynamic susceptibility difference is strictly positive:
\[
 \boxed{\displaystyle\lim_{m\to\infty}
 (\mathcal S_{\rm blocks}-\mathcal S_{\rm alt})
 =\frac{(x-y)^2}{(1-x)(1-y)(1-xy)}>0.}
\]
No assertion that the blocked layout is a global maximizer is needed or made.

## Assumptions and scope
For integers \(n\ge3\) and \(1\le m<n\), let \(\sigma_j\in\{-1,+1\}\), with indices modulo \(n\), and Hamiltonian
\[
 H_b(\sigma;h)=-\sum_{j=0}^{n-1}J_j\sigma_j\sigma_{j+1}-h\sum_{j=0}^{n-1}\sigma_j,
 \qquad J_j=\begin{cases}J_{\rm strong},&b_j=1,\\J_{\rm weak},&b_j=0.\end{cases}
\]
Assume \(\beta>0\) and \(0<J_{\rm weak}<J_{\rm strong}<\infty\). Gibbs expectations refer to \(h=0\). The object of optimization is \(\mathcal S_b=\operatorname{Var}_b(M)/n\) at fixed \(n,m,\beta,J_{\rm strong},J_{\rm weak}\), varying only \(b\) with \(\sum b_j=m\). A circular word is *balanced* if, for every arc length, its numbers of strong bonds on different cyclic arcs of that length differ by at most one. The floor-defined word in the Finding is balanced.

## Proof
**1. Exact two-point function.** Put \(t_j=\tanh(\beta J_j)\) and \(P=\prod_jt_j\). Using
\[
 e^{\beta J_j\sigma_j\sigma_{j+1}}=\cosh(\beta J_j)(1+t_j\sigma_j\sigma_{j+1}),
\]
the spin sum vanishes for a chosen edge subset unless all vertex degrees in that subset are even. On a single cycle only the empty and full edge subsets satisfy this. Therefore
\[
 Z_b(\beta,0)=2^n\prod_j\cosh(\beta J_j)(1+P).
\]
For distinct vertices \(u,v\), the spin insertion \(\sigma_u\sigma_v\) instead selects precisely one of the two complementary simple arcs between them. If \(T_{uv}\) is the product of \(t_j\) along either one of these arcs, then
\[
 \langle\sigma_u\sigma_v\rangle_b=\frac{T_{uv}+P/T_{uv}}{1+P}.
\]
Spin-flip symmetry gives \(\langle M\rangle_b=0\). Summing over all unordered vertex pairs, equivalently over all nonempty proper directed cyclic edge arcs, yields
\[
 \operatorname{Var}_b(M)=n+\frac{2}{1+P}\sum_{k=1}^{n-1}\sum_{i=0}^{n-1}
 \prod_{j=0}^{k-1}t_{i+j\bmod n}.
\tag{1}
\]
This formula is exact for every allowed size and all positive couplings.

**2. Independent convex lower bound for every arc length.** For binary assignments \(b_j\), define the strong-bond count
\[
 c_{i,k}=\sum_{j=0}^{k-1}b_{i+j\bmod n},\qquad
 \sum_{i=0}^{n-1}c_{i,k}=km.
\]
The inner sum in (1) is \(y^k\sum_iq^{c_{i,k}}\). Since \(q>1\), the strictly convex function \(z\mapsto q^z\) implies that among integer vectors with \(n\) entries summing to \(km\), the unique minimizing multiset consists of \(n-s_k\) entries equal to \(r_k\) and \(s_k\) equal to \(r_k+1\). Indeed if two entries \(a\le b-2\) occur, changing them to \(a+1,b-1\) reduces the sum by
\[
 (q-1)(q^{b-1}-q^a)>0.
\]
This gives the stated lower bound separately for every \(k\).

**3. Simultaneous attainment and exact equality conditions.** The mechanical word
\[
 b_j=\lfloor(j+1)m/n\rfloor-\lfloor jm/n\rfloor
\]
contains exactly \(m\) ones, and every cyclic length-\(k\) arc contains either \(\lfloor km/n\rfloor\) or \(\lceil km/n\rceil\) ones, by the floor identity and period \(n\). Thus it attains every convex lower bound simultaneously, proving the exact minimum in the Finding. Conversely, strict convexity means that any global minimizer must be circularly balanced at **every** arc length.

For completeness, circular balance determines one rotation orbit. Let \(S_j=\sum_{i=0}^{j-1}b_i\) for \(0\le j\le n\), and put \(d_j=S_j-jm/n\). For any \(0\le i<j\le n\), circular balance and the average window count imply \(S_j-S_i\in\{\lfloor(j-i)m/n\rfloor,\lceil(j-i)m/n\rceil\); hence \(|d_j-d_i|<1\) unless the difference is exactly zero. Therefore \(\max_jd_j-\min_jd_j<1\). Taking \(\alpha=\max_jd_j\in[0,1)\), one has \(0\le\alpha-d_j<1\), hence
\[
 S_j=\lfloor jm/n+\alpha\rfloor,
 \qquad b_j=\lfloor(j+1)m/n+\alpha\rfloor-\lfloor jm/n+\alpha\rfloor.
\]
Write \(m/n=p/q_0\) in lowest terms. As \(\alpha\) varies through a unit interval, these mechanical sequences have at most \(q_0\) different phases, separated by the residue grid \(\{r/q_0\}\). Shifting the word by one site changes the phase by \(p/q_0\) modulo one. Since \(p\) is coprime to \(q_0\), cyclic shifts visit all phases. Every minimizing word is therefore a rotation of the displayed mechanical word. This proves strict global uniqueness modulo rotation.

**4. Infinite-volume equimolar comparison.** In an alternating word, the proportion of strong bonds in a length-\(k\) arc is exactly \(k/2\) for even \(k\), and takes the two adjacent integers with equal frequency for odd \(k\). Thus for fixed \(k\), as the even ring length tends to infinity, the averaged arc product equals \((xy)^{k/2}\) for even \(k\), and \((x+y)(xy)^{(k-1)/2}/2\) for odd \(k\). For the two macroscopic blocks it converges to \((x^k+y^k)/2\) at fixed \(k\), since the number of arcs meeting either block boundary is at most \(2k\). All arc products are bounded by \(x^k\), and \(P\to0\). Dominated convergence for the geometric sum over \(k\) gives the two displayed thermodynamic formulas. Algebraic subtraction gives the positive-square expression for their difference.

More generally, if \(m/n\to\rho\in[0,1]\) along balanced rings, write \(k\rho=a_k+\theta_k\) with \(a_k=\lfloor k\rho\rfloor\) and \(0\le\theta_k<1\). The minimum has the well-defined limit
\[
 \lim_{n\to\infty}\mathcal S_{\min}=1+2\sum_{k=1}^\infty y^k
 \big[(1-\theta_k)q^{a_k}+\theta_kq^{a_k+1}\big].
\]
The series converges absolutely, because each averaged arc product is bounded by \(x^k\). The equimolar formula follows at \(\rho=1/2\).

## Verification
The standalone standard-library program `verify_ising.py` evaluates (1) using exact rational arithmetic and compares it with the closed minimum, including exhaustive assignment searches through \(n=12\). It also computes the zero-field Gibbs second moment independently by summing all spin configurations for smaller systems. A completed execution reported 8,164 exact assignment comparisons, 238 independent exact spin-ensemble comparisons, and 65 separate composition minima. It checks distinct coupling contrasts and approaches to both infinite-volume formulas. These checks corroborate the proof; the all-size statement follows from the convexity and balance arguments above.

Run from the same directory: `python3 verify_ising.py`. The program requires only the Python standard library.

## Relationship to prior work
Bhattacharya and Paul (2003) study transfer matrices, partition functions and Fibonacci bond order in periodic and quasiperiodic Ising chains. The present work uses the standard zero-field expansion but addresses a different global optimization: susceptibility at fixed finite bond composition, simultaneously at every positive temperature. Fici (2013) establishes combinatorial relationships among balanced, Sturmian and Christoffel words; their structure is prior theory, not a novelty claim here. Van Enter, Koivusalo and Miękisz (2019) construct lattice-gas Hamiltonians exhibiting Sturmian ground-state order; their zero-temperature interaction construction does not calculate or optimize the present nearest-neighbor Ising ring's positive-temperature magnetic susceptibility.

The asserted contribution is the strict all-compositions Ising susceptibility minimum, its evaluated finite-size formula, and the positive macroscopic segregation penalty. It is possible that a general cyclic-window rearrangement result or an earlier Ising susceptibility optimization implies parts of this theorem; no exhaustive uniqueness claim about the literature is made.

## Limitations
The physical model is classical, nearest-neighbor, spin-\(1/2\), ferromagnetic, finite-range and zero-field. Both couplings are strictly positive and distinct and temperature is strictly positive; zero temperature and vanishing-coupling boundary cases are excluded from uniqueness. The conclusion optimizes the *uniform-field linear-response susceptibility*, not nonlinear response, dynamics, critical exponents, or susceptibility at nonzero magnetic field. The two-block configuration is used for a contrast calculation, not asserted to maximize susceptibility. 

## References
1. S. Bhattacharya and S. K. Paul, *Ising Model on periodic and quasi-periodic chains in presence of magnetic field: some exact results*, arXiv:cond-mat/0306600v1 (first posted 2003-06-24), https://arxiv.org/abs/cond-mat/0306600.
2. G. Fici, *On the Structure of Bispecial Sturmian Words*, arXiv:1311.4904v1 (first posted 2013-11-19), https://arxiv.org/abs/1311.4904.
3. A. van Enter, H. Koivusalo and J. Miękisz, *Sturmian ground states in classical lattice-gas models*, arXiv:1906.12103 (first posted 2019-06-28), https://arxiv.org/abs/1906.12103.
