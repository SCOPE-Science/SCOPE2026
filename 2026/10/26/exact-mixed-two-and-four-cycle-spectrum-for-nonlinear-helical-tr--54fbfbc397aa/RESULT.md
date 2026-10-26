# Exact mixed two- and four-cycle spectrum for nonlinear helical transposition maps

## Finding

**Theorem (complete nonlinear-transposition cycle census).** Let \(n\ge3\), \(q=2^n\), and let \(V=\mathbb F_2^n\) with its additive group law. Choose distinct nonzero elements \(w,z\in V\), put \(d=w+z\), and let \(\tau\) exchange \(w\) and \(z\) while fixing every other element. For any shift \(c\in V\), set \(f_c(s)=\tau(s+c)\). The map \(f_c\) satisfies the characteristic-two Yang–Baxter-type functional equation
\[
f_c(x)+f_c(x+f_c(y))=f_c(x+f_c(y+f_c(x))).
\]
For every number \(m\ge1\) of sites, let \(T_{m,c}\) be the helical carrier sweep of the local rule
\[
R_{f_c}(x,b)=(b+f_c(x+b),\ x+f_c(x+b)),
\]
acting on the **complete** state \((x_1,\ldots,x_m,b_0)\in V^{m+1}\). Define \(F_j=\#\operatorname{Fix}(T_{m,c}^{\,j})\). Then \(T_{m,c}^4\) is the identity, and
\[
F_1=\begin{cases}
q(q-2)^m,&c=0,\\
q\,2^m,&c=d,\\
0,&c\notin\{0,d\},
\end{cases}
\qquad
F_2=\begin{cases}
q(q-4)^m,&m\ \text{even and }c\notin\{0,d\},\\
q^{m+1},&\text{otherwise}.
\end{cases}
\]
Consequently the exact numbers of **primitive full-state cycles** of lengths one, two, and four are, respectively,
\[
\boxed{\left(C_1,C_2,C_4\right)=
\left(F_1,\frac{F_2-F_1}{2},\frac{q^{m+1}-F_2}{4}\right).}
\]
In the mixed regime (\(m\) even and \(c\notin\{0,d\}\)), two-cycles and four-cycles both exist, and the fraction of all full states lying on four-cycles is exactly
\[
\boxed{1-\left(1-\frac4q\right)^m.}
\]
At fixed \(q\), the two-cycle fraction is positive at every even finite \(m\) but decays exponentially as \(m\to\infty\). Each \(f_c\) is genuinely **nonlinear** as a map of \(V\) when \(n\ge3\).

## Assumptions and scope

The field structure is used only through addition; no multiplicative property is required. In every sweep, process sites \(i=1,\ldots,m\) sequentially: given incoming carrier \(b_{i-1}\), put \((x_i',b_i)=R_{f_c}(x_i,b_{i-1})\), and retain the final carrier \(b_m\). The state being counted includes the carrier. Distinct points of a primitive \(j\)-cycle are counted together as one cycle. The parameter \(c\) can be arbitrary in \(V\), but \(w,z\) must be distinct and nonzero and \(n\ge3\). All equalities are exact for every admissible parameter and lattice length. The theorem does not classify general nonlinear Yang–Baxter maps, which need not be transpositions.

Write \(H=\{0,d\}\) and \(\overline V=V/H\); a bar denotes the image of an element under the quotient map. Since \(\overline w=\overline z\), the transposition is exactly
\[
f_c(s)=s+c+d\,\mathbf1_{\{\overline{s+c}=\overline w\}}.
\]

## Proof

**1. Admissibility and nonlinearity.** More generally, if \(g:\overline V\to H\) is any function, the map \(f(s)=s+c+g(\bar s)\) satisfies the displayed functional equation: because adding any element of \(H\) leaves quotient classes unchanged, each side simplifies to
\[
y+c+g(\bar x)+g(\bar y)+g(\overline{x+y+c}).
\]
Our map uses \(g(\bar s)=d\,\mathbf1_{\{\bar s+\bar c=\bar w\}}\). Suppose \(f_c\) were affine over \(\mathbb F_2\). Then \(f_c(s)+s+c\) would be an affine map into \(H\) whose nonzero fiber has exactly two elements. Any nonconstant affine map from \(V\) onto the one-dimensional group \(H\) has exactly \(q/2\) points in either fiber. But \(q/2\ge4\), and the perturbation is not constant. This is impossible. Thus these admissible examples are nonlinear.

**2. One-sweep quotient dynamics.** Put
\[
A_i(t)=\mathbf1_{\{\overline{x_i(t)+b_{i-1}(t)+c}=\bar w\}},
\qquad e_i(t)=c+dA_i(t).
\]
The local rule, after cancellation in characteristic two, has the remarkably simple form
\[
R_{f_c}(x,b)=(x+e,b+e).
\]
Hence site \(i\) gains \(e_i(t)\), and the carrier after site \(i\) gains the same increment. Modulo \(H\), every increment is \(\bar c\). Therefore, for any integer \(t\ge0\),
\[
\overline{x_i(t)}=\overline{x_i(0)}+t\bar c,
\quad \overline{b_0(t)}=\overline{b_0(0)}+tm\bar c,
\quad \overline{b_{i-1}(t)}=\overline{b_0(t)}+(i-1)\bar c.
\]
Substitution yields the exact indicator identity
\[
\boxed{A_i(t)=\mathbf1_{\{\overline{x_i(0)}+\overline{b_0(0)}+i\bar c+t(m+1)\bar c=\bar w\}}.}
\]

**3. Two-sweep classification.** If \(m\) is odd, or \(\bar c=0\), the coefficient \((m+1)\bar c\) vanishes in characteristic two. Thus \(A_i(t)\) does not change with \(t\), each pair of site increments cancels, and the carrier increments cancel as well. Hence \(T_{m,c}^2\) is the identity.

Suppose instead that \(m\) is even and \(\bar c\ne0\), equivalently \(c\notin\{0,d\}\). Consecutive indicators test the distinct cosets \(\bar w\) and \(\bar w+\bar c\). Their sum \(B_i=A_i(t)+A_i(t+1)\), calculated in \(\mathbb F_2\), is independent of \(t\) and equals one exactly when
\[
\overline{x_i(0)}+\overline{b_0(0)}+i\bar c
\in\{\bar w,\bar w+\bar c\}.
\]
Summing the two site updates gives \(x_i(t+2)=x_i(t)+dB_i\); summing carrier increments gives \(b_0(t+2)=b_0(t)+d\sum_iB_i\). Since every \(B_i\) is invariant under further sweeps, applying this translation twice yields \(T_{m,c}^4=\mathrm{id}\).

Crucially, \(T_{m,c}^2\) fixes the **full state** precisely when all \(B_i=0\): if any \(B_i=1\), site \(i\) changes by the nonzero vector \(d\). For each freely chosen initial carrier (\(q\) choices), the condition \(B_i=0\) excludes exactly two distinct cosets of \(H\), or four values of each site. Choices are independent across sites, so \(F_2=q(q-4)^m\) in the mixed regime. In the other regimes, \(F_2=q^{m+1}\).

**4. Fixed states and primitive cycles.** A full state is fixed under one sweep if and only if every local increment \(e_i=c+dA_i\) is zero: site coordinates are updated exactly once per sweep, and if no site changes the final carrier does not change either. For \(c=0\), this means \(A_i=0\) at every site, giving \(q-2\) independent site choices for each carrier. For \(c=d\), it means \(A_i=1\) at every site, giving two choices per site for each carrier. For any other \(c\), neither allowed increment \(c\) nor \(c+d\) is zero, so no full state is fixed. This proves the formula for \(F_1\). Since \(T^4=\mathrm{id}\), all primitive periods divide four, and subtracting fixed-point counts gives exactly \(C_1=F_1\), \(C_2=(F_2-F_1)/2\), and \(C_4=(q^{m+1}-F_2)/4\). In the mixed regime \(q\ge8\) ensures \(q(q-4)^m>0\) and \(q^{m+1}>q(q-4)^m\), proving coexistence and the stated proportions.

## Verification

Run `python3 verify.py` (Python standard library only). The checker verifies the functional equation directly on the whole \(8\)-element state alphabet for every unordered pair of distinct nonzero swapped symbols and every shift, then exhaustively enumerates every full configuration for lattice lengths one through three. These are \(504\) parameter/length combinations, including the complete carrier state. It also checks \(16\) selected cases on \(16\) symbols and lattice lengths one and two, replays four sweeps, and checks both fixed-point counts and primitive-cycle integrality. The exact mixed example with \(q=8\), \(w=1\), \(z=2\), \(c=4\), and \(m=2\) has \((C_1,C_2,C_4)=(0,64,96)\), accounting for all \(512\) full states. The unbounded statements are established by the proof, not by these finite tests. `verification_output.txt` records the checker output.

## Relationship to prior work

Araoka and Tokihiro's public preprint, *Integrable cellular automata on finite fields of order \(2^n\)* (arXiv:2602.17148v1, first public 2026-02-19), defines the local Yang–Baxter map and helical carrier sweep, constructs admissible transpositions and shifts, and reports period-two/four behavior in low field dimensions. These contributions are prior. The present theorem establishes the **complete primitive full-state orbit census** for every shifted one-transposition rule in every field dimension \(n\ge3\), with an exact mixed-period phase-space fraction. In contrast, the public note *Complete cycle census for additive-affine helical Yang–Baxter automata* (2026) classifies only additive-affine rules; its even-length period-four criterion yields uniformly period-four orbits, and does not cover this genuinely nonlinear mixed-period family. The universal identity \(C_j=P_j/j\) for periodic-point counts is elementary and is not claimed as new: the contribution is the explicit determination of \(F_1\) and \(F_2\) for the nonlinear family.

## Limitations

All claims count the carrier together with sites; projecting out the carrier can shorten periods. The study is restricted to single transpositions with two distinct nonzero swapped elements and their shifts; it does not establish a period-four bound for arbitrary nonlinear admissible maps. No assertion is made about arbitrary finite-field characteristic, spatially infinite maps, or entropy. A wider historical result in nonlinear Yang–Baxter orbit combinatorics might imply the census, and the later journal version's complete text was not independently read. Independent mathematical and priority validation remain outstanding.

## References

1. Aoi Araoka and Tetsuji Tokihiro, *Integrable cellular automata on finite fields of order \(2^n\)*, arXiv:2602.17148v1 (2026-02-19), https://arxiv.org/html/2602.17148.
2. Aoi Araoka and Tetsuji Tokihiro, journal record, *Mathematical Physics, Analysis and Geometry* 29 (2026), DOI:10.1007/s11040-026-09569-9.
3. *Complete cycle census for additive-affine helical Yang–Baxter automata* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-cycle-census-for-additive-affine-helical-yang-baxter-au--69b4a05d6a01.
