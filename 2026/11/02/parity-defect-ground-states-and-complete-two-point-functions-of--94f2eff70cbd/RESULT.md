# Parity-defect ground states and complete two-point functions of antiprism Ising antiferromagnets

## Finding
For every integer \(n\ge3\), let \(A_n\) be the labelled \(n\)-antiprism graph on \(a_i,b_i\) (\(i\in\mathbb Z/n\mathbb Z\)), with edges \(a_ia_{i+1}\), \(b_ib_{i+1}\), \(a_ib_i\), and \(a_{i+1}b_i\). Put classical spins \(\sigma_v\in\{\pm1\}\) on the vertices and take uniform antiferromagnetic exchange \(H=J\sum_{uv\in E(A_n)}\sigma_u\sigma_v\), where \(J>0\), with zero external field.

The exact minimum exchange energy and the number of *labelled* spin ground states are
\[
E_0=\begin{cases}-2nJ,&n\text{ even},\\-2(n-1)J,&n\text{ odd},\end{cases}
\qquad
G_n=\begin{cases}4,&n\text{ even},\\2n^2,&n\text{ odd}.\end{cases}
\]
For even \(n\), all four ground states have magnetization \(M=\sum_v\sigma_v=0\). For odd \(n\), the *complete* ground-state magnetization distribution is
\[
G_n(M)=\begin{cases}n(n+1),&M=0,\\n(n-1)/2,&M=2\text{ or }M=-2,\\0,&\text{otherwise}.\end{cases}
\]
In the uniform zero-field ground-state measure write \(C_{aa}(r)=\langle\sigma_{a_0}\sigma_{a_r}\rangle\) and \(C_{ab}(r)=\langle\sigma_{a_0}\sigma_{b_r}\rangle\), for each \(0\le r<n\). The *complete* two-point functions are
\[
\begin{array}{c|cc}
 & C_{aa}(r)=C_{bb}(r) & C_{ab}(r)\\\hline
n\text{ even}&(-1)^r&0\\
n\text{ odd}&(-1)^r(1-2r/n)&(-1)^{r+1}(n+2r(n-r-1))/n^2.
\end{array}
\]
All remaining ordered correlations follow from cyclic translation and exchange of the two vertices: in particular \(C_{ba}(r)=C_{ab}((-r)\bmod n)\). At fixed positive odd \(n\), the zero-field susceptibility \(\chi_n(T)=\partial_h\langle M\rangle_{T,h}|_{h=0}\) for \(H_h=H-hM\) satisfies, in units \(k_B=1\),
\[
\lim_{T\downarrow0}T\chi_n(T)=2(n-1)/n.
\]
The corresponding coefficient is zero for even \(n\). Thus odd rings have a finite-size Curie divergence and \(2n^2\) ground states whereas even rings have exactly four nonmagnetic ground states. For odd \(n\), \(C_{ab}(r)=O(n^{-1})\) at fixed \(r\), but if \(r/n\to x\in(0,1)\), then \((-1)^{r+1}C_{ab}(r)\to2x(1-x)\): the large-size and large-separation limits do not commute.

## Assumptions and scope
This is a finite, labelled, simple graph for each integer \(n\ge3\), with exactly \(2n\) vertices and \(4n\) edges. Indices are cyclic. The equivalent description as the square \(C_{2n}^2\) of a cycle makes this a periodic, equally antiferromagnetic nearest/next-nearest-neighbour Ising chain. All displayed expectations are *uniform averages over all zero-field ground states*, equivalently the \(T\downarrow0\) Gibbs limit at \(h=0\) for fixed \(n\). No order of thermodynamic, zero-temperature, or weak-field limits is silently exchanged. Spin assignments related by rotation or global spin reversal are counted separately.

## Proof
**1. A sharp triangular-frustration lower bound.** Call an edge frustrated when its endpoints have equal spins. There are two triangular faces per index,
\(T_i=(a_i,a_{i+1},b_i)\) and \(U_i=(a_{i+1},b_i,b_{i+1})\).
Each triangle has either one or three frustrated edges, hence at least one. Let \(R_a,R_b\) be the respective numbers of frustrated outer and inner rim edges, and \(I\) the number of frustrated cross edges. Every rim edge lies in one of these triangles, and every cross edge in two. Consequently
\[
R_a+R_b+2I\ge2n,
\qquad F=R_a+R_b+I\ge n+(R_a+R_b)/2.
\]
Because a cycle of length \(n\) has an even number of antialigned edges, \(R_a\equiv R_b\equiv n\pmod2\). For even \(n\) we obtain \(F\ge n\); for odd \(n\), \(F\ge n+1\). Since \(H=J(2F-4n)\), these bounds imply the claimed energy bounds.

**2. Classification of equality, even case.** Equality \(F=n\) when \(n\) is even forces \(R_a=R_b=0\), so both rims alternate. Conversely any independent choice of the two starting spins, with both rims alternating, makes precisely one cross edge frustrated in each pair of adjacent triangles and achieves \(F=n\). There are exactly four such states, all with \(M=0\). Averaging their independent rim phases yields \(C_{aa}(r)=C_{bb}(r)=(-1)^r\) and \(C_{ab}(r)=0\).

**3. Classification of equality, odd case.** Equality \(F=n+1\) forces \(R_a=R_b=1\) and *exactly one* frustrated edge in every triangular face. Let the unique frustrated rim edges have indices \(I\) (top) and \(K\) (bottom). There are \(n\) choices for each. The top rim is then completely determined by one spin \(a_0\); the bottom rim by one spin \(b_0\). Every triangle whose rim edge is antialigned already has exactly one frustrated edge, irrespective of the third spin. Only the two triangles sitting on the rim defects need checking. The top-defect triangle requires \(b_I=-a_I\), while the bottom-defect triangle requires \(a_{K+1}=-b_K\). Those conditions are equivalent: if \(I\le K\), the paths \(a_I\to a_{K+1}\) and \(b_I\to b_K\) contain respectively one and zero defective rim edges, and both spin ratios are \((-1)^{K-I}\); if \(I>K\), the reverse paths from \(a_{K+1}\) to \(a_I\) and from \(b_K\) to \(b_I\) contain respectively zero and one defective rim edges, and both spin ratios are \((-1)^{I-K-1}\). Therefore \(a_{K+1}b_K=a_Ib_I\) in either case. The single constraint \(b_I=-a_I\) leaves exactly two global spin-reversed states per pair \((I,K)\), all attaining \(F=n+1\). Hence \(G_n=2n^2\), with no further states.

**4. Magnetization distribution.** A single-frustrated-edge antiferromagnetic odd cycle has layer magnetization \(\pm1\). The displayed rim formulas imply \(M_a=a_0(-1)^I\) and \(M_b=b_0(-1)^K\). Since \(b_0=-a_0(-1)^{{\bf1}_{K<I}}\), the majority-spin ratio is \(M_b/M_a=-(-1)^{K-I+{\bf1}_{K<I}}\). For odd \(n\), this equals \(-(-1)^{(K-I)\bmod n}\). Thus the two layer majority spins coincide exactly when the forward residue \((K-I)\bmod n\) is odd; otherwise they oppose. For each \(I\), precisely \((n-1)/2\) choices of \(K\) give coinciding majorities, and \((n+1)/2\) give opposing ones. The two global spin orientations then provide one \(M=2\) and one \(M=-2\) state in each former case, and two \(M=0\) states in each latter case, yielding the stated counts.

**5. Every two-point function.** With \(I,K\) independent and uniform in \(\{0,\ldots,n-1\}\), traversing \(r\) successive rim edges flips the spin on every edge except its one defect. Thus \(\langle a_0a_r\rangle=(-1)^r(1-2r/n)\), and likewise for the lower rim. To obtain the cross-layer correlation, for \(0\le t<n\) use
\[
a_t=a_0(-1)^t(-1)^{{\bf1}_{I<t}},\qquad
b_t=b_0(-1)^t(-1)^{{\bf1}_{K<t}}.
\]
The constraint \(b_I=-a_I\) gives \(b_0=-a_0(-1)^{{\bf1}_{K<I}}\). Hence
\[
a_0b_r=-(-1)^r(-1)^{{\bf1}_{K<I}+{\bf1}_{K<r}}.
\]
Averaging first over \(I\) and then over \(K\) yields
\[
C_{ab}(r)=-\frac{(-1)^r}{n^2}\sum_{k=0}^{n-1}(2k+2-n)(-1)^{{\bf1}_{k<r}}
=\frac{(-1)^{r+1}}{n^2}\bigl(n+2r(n-r-1)\bigr).
\]
The final asymptotic claims follow directly. The zero-field Gibbs susceptibility satisfies \(T\chi_n(T)=\operatorname{Var}_{T,0}(M)\); the finite-state zero-temperature limit is the uniform ground-state variance, \(2(n-1)/n\) for odd \(n\) and zero for even \(n\). This completes the proof.

## Verification
Run `python3 verify.py` with the Python standard library. Three logically different finite checks are implemented: direct enumeration of all spin states for \(3\le n\le9\); an independent four-state periodic transfer recursion for \(3\le n\le34\); and explicit ground-state construction plus exact rational correlation sums for \(3\le n\le51\). The observed output is `VERIFY_OK brute_n=7 transfer_n=32 constructive_n=49`. Each check tests the energy, complete magnetization counts, and (where relevant) the two-point functions. The proof, not the finite computations, establishes the result for every \(n\ge3\).

## Relationship to prior work
The antiprism graph's identity with \(C_{2n}^2\) is standard [1]; this explains its connection to equal-coupling, competing first- and second-neighbor Ising chains. Moessner and Sondhi [2] study frustration and quantum perturbations on other lattices, including quasi-one-dimensional examples; their results do not provide the labelled-antiprism finite-cycle ground-state counting and full correlation formulas proved here. Mosseri [3] provides an arbitrary-graph Hadamard transform for computing Ising energy spectra; it is an algorithmic framework rather than a symbolic all-size antiprism solution. Jurčišinová and Jurčišin [4] solve an infinite zigzag Ising ladder with multisite interactions, including ground-state phases, by transfer matrices; finite circumference parity counts and the two-layer correlation kernels above are not established in the accessible abstract. Williams [5] studies ground-state properties and nearest-neighbor correlations of several frustrated chains, but the accessible abstract does not permit a decisive full-text comparison with the present finite-periodic result. The explicit all-\(n\) parity classification and full two-layer correlations are the assessed contribution, not the general existence of transfer methods, geometric frustration, or the antiprism graph itself.

## Limitations
The result is restricted to homogeneous positive \(J\), Ising spins \(\pm1\), zero external field for ground-state classification, and periodic \(n\)-antiprism graphs with \(n\ge3\). The susceptibility conclusion concerns the \(T\downarrow0\) limit at fixed finite \(n\). No complete nonzero-field phase diagram, finite-temperature closed partition function, quantum dynamics, or extension to nonuniform edge couplings is claimed. Prior literature on finite zigzag Ising chains may contain alternative forms of some formulas and warrants historical-priority review. No independent scientific audit has been conducted.

## References
[1] E. W. Weisstein, "Antiprism Graph," Wolfram MathWorld, https://mathworld.wolfram.com/AntiprismGraph.html .

[2] R. Moessner and S. L. Sondhi, "Ising models of quantum frustration," arXiv:cond-mat/0011250 (first posted 2000-11-15), https://arxiv.org/abs/cond-mat/0011250 .

[3] R. Mosseri, "Ising-like models on arbitrary graphs: The Hadamard way," arXiv:1409.0147 (first posted 2014-08-30), https://arxiv.org/abs/1409.0147 .

[4] E. Jurčišinová and M. Jurčišin, "Solution of the antiferromagnetic Ising model with multisite interaction on a zigzag ladder," *Physical Review E* 90, 032108 (2014), https://doi.org/10.1103/PhysRevE.90.032108 .

[5] J. K. Williams, "Ground state properties of frustrated Ising chains," *Journal of Physics C* 14, 4095 (1981), https://doi.org/10.1088/0022-3719/14/28/011 .
