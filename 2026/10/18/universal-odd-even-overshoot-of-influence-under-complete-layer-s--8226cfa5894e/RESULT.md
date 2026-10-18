# Universal odd–even overshoot of influence under complete-layer switching

## Finding

In a two-layer synchronous averaging model, a uniformly weighted complete-graph layer is applied for \(k\) steps, followed by one step of a connected weighted undirected social-network layer. The long-run influence distribution obeys a strict odd–even interlacing law for **every irregular admissible social graph**, rather than merely for a selected example.

Let \(n\ge 3\), let \(A\) denote complete-graph averaging without self-loops, let \(B\) denote the random-walk averaging matrix on the second graph, and define \(C_k=BA^k\). Write \(u\) for the uniform probability row vector and \(\pi\) for the degree-stationary probability row vector of \(B\). If \(\nu_k\) is the unique stationary probability row vector of \(C_k\), set
\[
\mathcal D_k=\chi^2(\nu_k\|\pi)
=\sum_{i=1}^{n}\frac{(\nu_{k,i}-\pi_i)^2}{\pi_i},
\qquad \mathcal D_A=\chi^2(u\|\pi).
\]
For every such graph with **nonconstant weighted degrees**, the strict chains are
\[
0<\mathcal D_2<\mathcal D_4<\cdots<\mathcal D_A
<\cdots<\mathcal D_5<\mathcal D_3<\mathcal D_1.
\]
Thus one, three, five, and every other odd number of complete-layer steps amplify influence disparity beyond the complete layer itself, whereas even numbers attenuate that disparity relative to the complete layer. Both parity subsequences converge to \(\mathcal D_A\) from opposite sides. If weighted degrees are constant, every displayed divergence is zero, so degree irregularity is the exact condition for the strict effect within this class.

The same parity effect has a directly observable consensus witness: take the initial opinion of agent \(i\) to be \(x_i=d_{\min}/d_i\), where \(d_i\) is their weighted degree and \(d_{\min}\) is the minimum weighted degree. For the isolated-layer consensus values \(c_B\) and \(c_A\), and the period-\(k+1\) switching consensus \(c_k\), every irregular admissible graph satisfies
\[
c_B<c_2<c_4<\cdots<c_A<\cdots<c_5<c_3<c_1.
\]
In particular, *each odd switching period yields consensus strictly outside the interval between the two isolated-layer consensus values*. The claim concerns this specified initial opinion, not every possible initial opinion.

The convergence factor per full switching cycle is also exact:
\[
\rho_2(C_k)=\frac{\rho_2(B)}{(n-1)^k}.
\]
Here \(\rho_2\) is the largest modulus among non-Perron eigenvalues. For an irregular graph, the worst-case asymptotic per-step factor \(\rho_2(C_k)^{1/(k+1)}\) strictly decreases as \(k\) increases.

## Assumptions and scope

Take a finite connected, nonbipartite, undirected weighted graph \(G\) on vertices \(\{1,\ldots,n\}\), with no self-loops, a positive weight \(w_{ij}=w_{ji}\) on each edge, zero weight on nonedges, and at least two distinct neighbors at every vertex. Define
\[
d_i=\sum_{j=1}^n w_{ij},\qquad
B_{ij}=\frac{w_{ij}}{d_i},\qquad
\pi_i=\frac{d_i}{\sum_{j=1}^n d_j},\qquad
u_{A,i}=u_i=\frac1n,
\]
\[
A_{ij}=\begin{cases}0&i=j,\\1/(n-1)&i\ne j.\end{cases}
\]
All update matrices act on opinion column vectors on the left. A switching cycle consists of \(k\ge1\) updates by \(A\), then one update by \(B\), repeatedly; at the ends of cycles the update is \(C_k^m\) after \(m\) cycles. The hypotheses make \(A\), \(B\), and \(C_k\) primitive, so the individual and switched consensus values are well-defined for every bounded initial opinion column vector. Graph edge weights may be arbitrary positive real numbers; no genericity, upper-degree cutoff, or finite catalogue is assumed.

## Proof

**1. Exact reduction and strict positivity.** Let \(\mathbf 1\) be the all-ones column and \(P=\mathbf 1u\). Since \(P^2=P\), complete averaging has the two-eigenvalue decomposition
\[
A=P-\frac1{n-1}(I-P),\qquad
A^k=P+t_k(I-P),\qquad t_k=\left(-\frac1{n-1}\right)^k.
\]
Because \(BP=P\), multiplication gives the *exact* reduction
\[
C_k=(1-t_k)P+t_kB.\tag{1}
\]
For even \(k\), the entries of \(C_k\) are positive because \(0<t_k<1\). For odd \(k\ge3\), \(|t_k|<1/(n-1)\) and the entries remain positive from (1), using \(B_{ij}\le1\). For \(k=1\), direct multiplication gives \((BA)_{ij}=(1-B_{ij})/(n-1)>0\), as every vertex has at least two positive-weight neighbors. Thus \(C_k\) is positive for every \(k\ge1\). The primitive \(B\) has stationary distribution \(\pi\) by detailed balance \(\pi_i B_{ij}=w_{ij}/\sum_l d_l\).

**2. Exact stationary influence.** Put \(t=t_k\). The stationary relation \(\nu_k=\nu_k C_k\), together with (1), gives \(\nu_k(I-tB)=(1-t)u\). As \(|t|<1\) and \(B\) is stochastic, \(I-tB\) is invertible. Therefore
\[
\boxed{\nu_k=(1-t_k)u(I-t_kB)^{-1}.}\tag{2}
\]

**3. Reversible spectral expansion.** Regard column vectors as the real Hilbert space with inner product \(\langle f,g\rangle_\pi=\sum_i\pi_i f_i g_i\). Reversibility makes \(B\) self-adjoint here, with orthonormal eigenbasis \(\mathbf1,e_2,\ldots,e_n\) and real eigenvalues \(1=\lambda_1>\lambda_j>-1\) for \(j\ge2\). Define the degree-imbalance density
\[
h_i=\frac{u_i}{\pi_i}=\frac{\sum_jd_j}{nd_i},\qquad
h=\mathbf1+g,\qquad
\langle \mathbf1,g\rangle_\pi=0,\qquad
g=\sum_{j=2}^n a_je_j.
\]
Detailed balance and (2) show that the density of \(\nu_k\) relative to \(\pi\) is
\[
\frac{\nu_{k,i}}{\pi_i}=
\left[(1-t)(I-tB)^{-1}h\right]_i
=1+\sum_{j=2}^n a_j f_{\lambda_j}(t)e_j(i),
\qquad f_\lambda(t)=\frac{1-t}{1-t\lambda}.\tag{3}
\]
The denominator is positive for \(-1<t<1\). Since \(\lambda<1\),
\[
 f_\lambda'(t)=\frac{\lambda-1}{(1-t\lambda)^2}<0,
\qquad f_\lambda(t)>0,\qquad f_\lambda(0)=1.\tag{4}
\]
Orthogonality in (3) gives the exact spectral certificate
\[
\boxed{\mathcal D_k=\sum_{j=2}^n a_j^2
\left(\frac{1-t_k}{1-t_k\lambda_j}\right)^2,\qquad
\mathcal D_A=\sum_{j=2}^n a_j^2.}\tag{5}
\]
Nonconstant degrees are equivalent to \(g\ne0\), hence to \(\sum_j a_j^2>0\). For even \(k\), \(t_k>0\) strictly decreases to zero and each factor in (5) strictly increases from a value below one. For odd \(k\), \(t_k<0\) strictly increases toward zero and each factor strictly decreases from a value above one. Equations (4)–(5) prove the asserted strict divergence chains; constant degrees give \(g=0\) and equality for all \(k\).

**4. A consensus opinion witness.** Set \(\eta=nd_{\min}/\sum_jd_j\), so the stipulated opinion vector is \(x=\eta h\), with every coordinate in \((0,1]\). For isolated averaging,
\[
c_B=\pi x=\eta,\qquad
c_A=ux=\eta(1+\mathcal D_A).
\]
For the switched chain, using (2), reversibility, and the same orthogonal expansion,
\[
\boxed{c_k=\nu_kx
=\eta\left[1+\sum_{j=2}^n a_j^2 f_{\lambda_j}(t_k)\right].}\tag{6}
\]
Replacing the squared factors in (5) by the positive first powers in (6) preserves all strict comparisons because every \(f_{\lambda_j}\) decreases in \(t\) and \(\sum_j a_j^2>0\). This proves the corresponding strict odd–even consensus chains.

**5. Exact contraction spectrum and strict time-normalized improvement.** The invariant line spanned by \(\mathbf1\) is fixed by \(C_k\). On the quotient by this line, \(P\) vanishes, so (1) acts as \(t_kB\). Its nontrivial eigenvalues are precisely \(t_k\lambda_j\), \(j\ge2\); the full eigenvalue \(1\) is simple. Consequently \(\rho_2(C_k)=|t_k|\rho_2(B)\).

Because \(B\) is loopless, \(\operatorname{tr}(B)=0\), hence \(\sum_{j=2}^n\lambda_j=-1\) and \(\rho_2(B)\ge 1/(n-1)\). Equality would force all non-Perron eigenvalues to equal \(-1/(n-1)\), so reversibility implies \(B=\mathbf1\pi-\frac1{n-1}(I-\mathbf1\pi)\). Its zero diagonal then forces \(\pi_i=1/n\), and hence \(B=A\). An irregular graph cannot satisfy this equality; therefore \((n-1)\rho_2(B)>1\). The exact worst-case per-update asymptotic factor is
\[
r_k=\bigl(\rho_2(C_k)\bigr)^{1/(k+1)}
=\frac1{n-1}\left[(n-1)\rho_2(B)\right]^{1/(k+1)},\tag{7}
\]
which is strictly decreasing in every integer \(k\ge1\). The claim concerns the worst-case spectral rate; particular initial opinions may converge faster when their leading spectral projections vanish.

## Verification

The standalone standard-library script `verify.py` checks four distinct irregular nonbipartite undirected weighted graphs on \(3\), \(4\), \(5\), and \(6\) vertices, for all twelve values \(1\le k\le12\). It recomputes \(BA^k\), (1), the exact stationary row distribution from (2), strict positivity, both parity chains for consensus and \(\chi^2\), and the quotient-space identity for two independent test vectors at every period. All scalar arithmetic uses rational fractions; these finite tests support, but do not prove, the all-graph claims.

For example, on the weighted triangle with edge weights \(w_{12}=2\), \(w_{13}=w_{23}=1\), the inverse-degree initial opinions are \((2/3,2/3,1)\). The exact isolated values and first four switched values are
\[
c_B=\frac34,\quad c_A=\frac79,\quad
c_1=\frac45,\quad c_2=\frac{10}{13},\quad
c_3=\frac{18}{23},\quad c_4=\frac{38}{49}.
\]
Thus the parity inequalities occur already on a three-agent graph and persist universally under the stated hypotheses.

## Relationship to prior work

Shiu and Naghizadeh introduced the periodically switched coordination model in their 2025 Allerton proceedings paper and expanded it in a 2026 preprint. The latter's Section IV-A gives one three-agent, one-step example in which stationary influence lies outside the interval between the individual-layer stationary influences. Its Propositions IV.1 and IV.3 give a primitivity criterion and a general convergence-rate bound, while Proposition IV.4 gives an asymptotic \(O(\rho_2(A)^k)\) consensus comparison as switching periods grow. These are acknowledged; neither states the all-irregular-graph strict odd–even \(\chi^2\) law, its canonical bounded-opinion witness for every odd period, or the exact rate (7) for a complete averaging layer.

Ordinary Markov-chain reversibility, spectral decompositions, and resolvent formulas are established tools; novelty is not asserted for those ingredients individually. A related 2025 work by Abedinzadeh and Akyol studies time-varying Friedkin–Johnsen dynamics, where persistent innate beliefs fundamentally change the update equation. The present claim is for a particular DeGroot coordination model without stubborn beliefs. General results on teleportation kernels or reversible Markov resolvents could potentially subsume part of the formula and remain a priority risk.

## Limitations

The result is exact for finite deterministic synchronous averaging, one uniform loopless complete layer, one connected nonbipartite undirected weighted layer with at least two neighbors at each vertex, and the specified switch order. It does not cover arbitrary first-layer topologies, directed second layers, asynchronous updates, finite-agent random update noise, or every initial opinion vector. The noninterpolation conclusion for the consensus value is proved for the specified inverse-degree initial opinions; the \(\chi^2\) conclusion concerns the stationary influence distribution itself and holds independently of initial opinions. The theorem is not an assertion of independent historical-priority verification.

## References

1. R.-A. Shiu and P. Naghizadeh, *Coordination Games on Multiplex Networks: Consensus and Convergence of Opinion Dynamics*, 61st Allerton Conference on Communication, Control, and Computing, September 17, 2025. https://hdl.handle.net/2142/130286 .
2. R.-A. Shiu and P. Naghizadeh, *Coordination Games on Multiplex Networks: Consensus, Convergence, and Stability of Opinion Dynamics*, arXiv:2603.07633v1, March 8, 2026. https://arxiv.org/abs/2603.07633 .
3. M. H. Abedinzadeh and E. Akyol, *Stability and Robustness of Time-Varying Opinion Dynamics: A Graph-Theoretic Approach*, arXiv:2510.01580v1, October 2, 2025. https://arxiv.org/abs/2510.01580 .
