# A parity-reversing twist law for period-two chip-firing orbits on cubic ladders

## Finding

For each integer \(n\geq3\), let \(P_n=C_n\square K_2\) be the labelled circular ladder (prism) with columns \(i\in\mathbb Z/n\mathbb Z\) and rows \(r\in\{0,1\}\). Let \(M_{2n}\) be the corresponding Möbius ladder: use the same \(n\) rungs and the same consecutive-column rail edges for columns \(0,\ldots,n-1\), but join the last and first columns with *crossed* rail edges rather than parallel rail edges. Both are connected simple cubic graphs on \(2n\) vertices.

Equip each graph with the synchronous degree-threshold parallel chip-firing map on nonnegative integral chip configurations: in one update every vertex holding at least its degree fires one chip to each neighbor. A primitive period-two orbit consists of two distinct chip configurations alternating under this update. Count each such two-configuration orbit exactly once, without identifying different graph automorphisms.

Let \(N_P(n)\) and \(N_M(n)\) denote these orbit numbers, and let \(U_n,V_n,W_n\) be the three integer sequences defined for \(n\ge0\) by
\[
\begin{array}{lll}
U_0=2,& U_1=12,&U_{n+2}=12U_{n+1}-U_n,\\
V_0=2,& V_1=-2,&V_{n+2}=-2V_{n+1}+V_n,\\
W_0=2,& W_1=-4,&W_{n+2}=-4W_{n+1}+W_n.
\end{array}
\]
Then the exact orbit census is
\[
\boxed{N_P(n)=\frac{4+2(-1)^n+U_n+2V_n+2W_n}{2}},
\qquad
\boxed{N_M(n)=\frac{2+U_n+2V_n-2W_n}{2}}.
\]
In particular, **twisting reverses the inequality according to the parity of the number of rungs**:
\[
\boxed{N_P(n)-N_M(n)=1+(-1)^n+2W_n},
\qquad
\begin{cases}
N_P(n)>N_M(n),&n\text{ even},\\
N_P(n)<N_M(n),&n\text{ odd}.
\end{cases}
\]
Put \(\Lambda=6+\sqrt{35}\) and \(\rho=2+\sqrt5\). Both orbit numbers have the same leading growth,
\[
N_P(n)\sim N_M(n)\sim\frac{\Lambda^n}{2},
\]
whereas the signed boundary-twist discrepancy obeys
\[
N_P(n)-N_M(n)\sim2(-1)^n\rho^n,
\qquad
\frac{N_P(n)-N_M(n)}{N_M(n)}
\sim4(-1)^n\left(\frac{\rho}{\Lambda}\right)^n.
\]
Thus the *absolute* effect of twisting is exponentially large but its *relative* effect is exponentially small.

## Assumptions and scope

The degree is always three, there are no sinks or graph loops, and all vertices are labelled. The graphs have \(n\ge3\) rungs, avoiding degenerate repeated rail edges. Chip heights are arbitrary nonnegative integers, not bounded in advance. Only **primitive temporal two-cycles** are counted; this is not a census of all periodic points or all basins. An orbit is counted once, rather than once for each of its two phases. The row-swap map used in the proof is a symmetry of the *configuration labels*, not an identification of different chip-firing orbits.

## Proof

**1. Exact two-cycle weights.** On any connected loopless finite graph \(G\), write \(d(v)\) for the degree and \(F_t(v)\in\{0,1\}\) for the firing indicator in round \(t\). If a chip configuration returns in two rounds, the sum of the two firing vectors lies in the kernel of the graph Laplacian. Connectedness implies \(F_0(v)+F_1(v)=k\), constant in \(v\). If \(k=0\) or \(k=2\), every vertex waits or fires in both rounds, hence the chip configuration is fixed after one update. For a *primitive* two-cycle, necessarily \(k=1\), so the two firing sets are complementary.

Let \(S\) be the firing set in the first phase and define the cross-cut degree
\[
c_v(S)=\#\{w\sim v:\mathbf1_S(w)\ne\mathbf1_S(v)\}.
\]
For a vertex in \(S\), the chip height in the first phase must be one of the \(c_v(S)\) integers
\(d(v),d(v)+1,\ldots,d(v)+c_v(S)-1\). For a vertex outside \(S\), it must be one of \(d(v)-c_v(S),\ldots,d(v)-1\). This follows by writing the net chip flow in one round and imposing the opposite threshold condition in the next round. These intervals are nonnegative and their choices are independent. Therefore the exact number of first-phase configurations for the prescribed firing set is \(\prod_v c_v(S)\). Since the two phases have complementary firing sets, each primitive orbit is counted twice, giving the general identity
\[
N_G=\frac12\sum_{S\subseteq V(G)}\prod_{v\in V(G)}c_v(S).
\]
This general identity is background for the particular evaluation below, not claimed as a new general-graph result.

**2. An exact width-two transfer.** Encode one column's membership in \(S\) by a binary pair \(q=(a,b)\in\{0,1\}^2\). For three consecutive columns \(p=(a_-,b_-),q=(a,b),r=(a_+,b_+)\), define
\[
\begin{split}
c_\mathrm{top}(p,q,r)&=[a\ne a_-]+[a\ne a_+]+[a\ne b],\\
c_\mathrm{bottom}(p,q,r)&=[b\ne b_-]+[b\ne b_+]+[b\ne a],\\
w(p,q,r)&=c_\mathrm{top}(p,q,r)c_\mathrm{bottom}(p,q,r),
\end{split}
\]
where brackets are zero-one indicators. There are sixteen ordered adjacent-column states \((p,q)\). Define the integral \(16\times16\) transfer matrix by
\[
T_{(p,q),(q',r)}=\begin{cases}w(p,q,r),&q'=q,\\0,&q'\ne q.\end{cases}
\]
Let \(J\) be the permutation matrix implementing row exchange in both columns: \((p,q)\mapsto(\bar p,\bar q)\), with \(\bar{(a,b)}=(b,a)\). Directly from the definitions, \(TJ=JT\) and \(J^2=I\).

For the untwisted closure, every summand in \(\operatorname{tr}(T^n)\) is exactly one labelled sequence of \(n\) columns, with the product of all \(2n\) cross-cut degrees. For the twisted closure, the final column is identified with the first after row exchange; this is exactly \(\operatorname{tr}(T^nJ)\). Hence
\[
N_P(n)=\tfrac12\operatorname{tr}(T^n),\qquad
N_M(n)=\tfrac12\operatorname{tr}(T^nJ).
\]

**3. Symmetry decomposition and characteristic factors.** The plus and minus eigenspaces of \(J\) on the sixteen column-pair states have dimensions ten and six. Construct them by taking the sum and, where nonzero, difference of the standard basis vectors in each two-element row-swap orbit. On these invariant spaces the two characteristic polynomials are, respectively,
\[
\begin{split}
\chi_+(z)&=(z-1)^3(z+1)(z^2-12z+1)(z^2+2z-1)^2,\\
\chi_-(z)&=(z-1)(z+1)(z^2+4z-1)^2.
\end{split}
\]
These are exact sixteen-state integer computations, checked by `verify_transfer.py`, which independently constructs the entries, symmetry basis, induced blocks and characteristic polynomials. For every positive \(n\), the trace of a power is the sum of powers of eigenvalues with algebraic multiplicities, even without diagonalizability. Therefore
\[
\begin{split}
\operatorname{tr}(T^n|_+)&=3+(-1)^n+U_n+2V_n,\\
\operatorname{tr}(T^n|_-)&=1+(-1)^n+2W_n.
\end{split}
\]
Adding these traces computes the prism count; subtracting computes the Möbius count, establishing both stated expressions and the exact difference.

**4. Sign and asymptotics.** The two roots associated with \(W_n\) are \(-2+\sqrt5\in(0,1)\) and \(-2-\sqrt5<-1\). Consequently \(W_n\) is positive for even \(n\), negative for odd \(n\), and has magnitude greater than one when \(n\ge3\). The finite parity correction \(1+(-1)^n\) cannot reverse that sign. The largest eigenvalue modulus of the other factors is \(\Lambda=6+\sqrt{35}>\rho\); the coefficient of \(\Lambda^n\) in each orbit count is \(1/2\). This proves the strict parity reversal and all stated asymptotics.

## Verification

Run `python3 verify_transfer.py` with SymPy to recompute both invariant-block characteristic polynomials and the exact enumerations for rung numbers three through ten. Independently, compile `verify_direct.cpp` using `g++ -std=c++17 -O2` and run it. That program uses **no transfer matrix**: it enumerates all \(2^{2n}\) labelled cut assignments for each of the two graphs for rung numbers three through ten, evaluates all cross-cut degrees from explicit graph adjacency, and compares integer counts. For rung numbers three and four, it also constructs **every individual chip configuration** associated with a nonzero-weight cut and verifies by two direct chip-firing steps that it has least period two and the claimed firing set. Outputs from these executions are provided in `transfer_output.txt` and `direct_output.txt`.

The first three orbit pairs are
\[
(N_P(3),N_M(3))=(757,909),\quad
(N_P(4),N_M(4))=(10440,9794),\quad
(N_P(5),N_M(5))=(118681,121409).
\]
The finite direct tests corroborate but do not replace the all-\(n\) transfer-matrix proof.

## Relationship to prior work

Jiang–Scully–Zhang study which firing patterns can occur and prove a general nonclumpiness restriction; they do not count the chip configurations in each two-cycle on these two graph families. Levine's complete-graph analysis studies mode locking and recurrent periods, not this twisted-boundary orbit census. Fey–Levine–Wilson investigate fixed-energy sandpile criticality on finite ladders, concentrating on density and stationary behavior rather than an exact primitive temporal two-orbit count for these cubic closures. A previously established general cut-degree expression determines two-cycle counts by a sum over all cuts; the **new evaluated result** here is the simultaneous closed recurrence and the strictly alternating sign of the difference under the Möbius twist. The new claim is not the underlying general cut-degree identity or the mere applicability of that identity to a prism graph.

## Limitations

The result concerns *exactly* primitive period-two orbits for the unweighted, loopless, synchronous model, and does not classify other periods or attraction basins. It counts labelled graph configurations without quotienting spatial symmetries. Structural priority is subject to unindexed or inaccessible equivalent computations. The exact recurrence follows from the stated transfer definition and can be reproduced without relying on a numerical extrapolation; separate formal or independent human mathematical review has not been conducted.

## References

1. Lionel Levine, *Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincaré Rotation Number*, first public arXiv posting 2008-11-17, arXiv:0811.2800, https://arxiv.org/abs/0811.2800.
2. Tian-Yi Jiang, Ziv Scully, Yan X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, first public arXiv posting 2012-11-29, arXiv:1211.6786, https://arxiv.org/abs/1211.6786; SIAM J. Discrete Math. 29 (2015), 615–630, DOI:10.1137/130933770.
3. Anne Fey, Lionel Levine, David B. Wilson, *The Approach to Criticality in Sandpiles*, Phys. Rev. E 82 (2010), 031121, DOI:10.1103/PhysRevE.82.031121; accessible full text https://ir.cwi.nl/pub/17204/17204D.pdf.
