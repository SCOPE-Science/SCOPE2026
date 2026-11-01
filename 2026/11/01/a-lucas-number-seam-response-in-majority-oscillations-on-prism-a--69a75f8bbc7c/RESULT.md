# A Lucas-number seam response in majority oscillations on prism and Möbius ladders

## Finding

For every integer \(n\ge3\), consider the two labelled cubic graphs on \(2n\) vertices: the prism \(P_n=C_n\square K_2\) and the Möbius ladder \(M_n\), formed from \(C_{2n}\) by adding the antipodal matching. Under synchronous binary strict-neighbor majority, let \(f_X(n)\) be the number of fixed configurations, \(q_X(n)\) the number of configurations that return after two updates, and \(b_X(n)=(q_X(n)-f_X(n))/2\) the number of primitive period-two orbits, with no quotient by graph symmetries.

Let the Lucas integers satisfy \(L_0=2\), \(L_1=1\), and \(L_{k+2}=L_{k+1}+L_k\), and put
\[
R_k=L_k+2\cos(k\pi/3).
\]
Then the **complete recurrent-orbit census** is
\[
f_P(n)=R_n+2,\qquad f_M(n)=R_n,
\]
\[
q_P(n)=\begin{cases}(R_n+2)^2,&n\text{ even},\\ R_{2n}+2,&n\text{ odd},\end{cases}
\qquad
q_M(n)=\begin{cases}R_{2n}+2,&n\text{ even},\\ R_n^2,&n\text{ odd}.\end{cases}
\]
Equivalently,
\[
b_P(n)=\begin{cases}(R_n+2)(R_n+1)/2,&n\text{ even},\\(R_{2n}-R_n)/2,&n\text{ odd},\end{cases}
\]
\[
b_M(n)=\begin{cases}(R_{2n}+2-R_n)/2,&n\text{ even},\\R_n(R_n-1)/2,&n\text{ odd}.\end{cases}
\]
In particular, the **exact twist response** obeys
\[
\boxed{b_P(n)-b_M(n)=
\begin{cases}
4L_n+6,&n\equiv0\pmod6,\\
-L_n,&n\equiv1,5\pmod6,\\
L_n,&n\equiv2,4\pmod6,\\
2L_n,&n\equiv3\pmod6.
\end{cases}}
\]
Thus inserting the Möbius seam increases the number of primitive two-cycles exactly when \(n\equiv1,5\pmod6\). With \(\phi=(1+\sqrt5)/2\), both populations satisfy \(b_P(n)\sim b_M(n)\sim\phi^{2n}/2\), whereas their difference has order \(\phi^n\) and changes sign with \(n\bmod6\).

## Assumptions and scope

All vertices are labelled. The graph \(P_n\) has vertices \((i,j)\), for \(i\in\mathbb Z/n\mathbb Z\), \(j\in\{0,1\}\), with edges between \((i,j)\) and \((i\pm1,j)\) and between \((i,0)\) and \((i,1)\). The graph \(M_n\) has vertices \(k\in\mathbb Z/(2n)\mathbb Z\), with edges to \(k\pm1\) and \(k+n\). These are simple, undirected, three-regular graphs for \(n\ge3\). Each vertex simultaneously adopts the strictly prevailing bit among its three neighbors; its previous bit is not included as an input. No tie-breaking convention is required. A primitive period-two orbit is an unordered pair \(\{x,F(x)\}\) with \(F^2(x)=x\ne F(x)\).

## Proof

**1. Fixed configurations.** View either ladder as two longitudinal rails joined by \(n\) rungs. If a rung has opposite bits, then for each of its endpoints to remain fixed, **both** horizontal neighbors must have the endpoint's bit. Thus the two neighboring rungs are likewise opposite and carry the same orientation. Propagating this condition forces both rails to be constant with opposite colors. This gives exactly two fixed states on the untwisted prism; on the Möbius ladder the identification at the twisted seam reverses the rail colors and makes such a state impossible. If no rung is opposite, its two endpoints have one common bit \(a_i\). This state is fixed precisely when no cyclic singleton occurs: \(a_{i-1}=a_{i+1}\ne a_i\) is forbidden for every \(i\). Therefore \(f_P=R_n+2\) and \(f_M=R_n\), once the singleton-free word count is established.

**2. Singleton-free transfer.** Index directed de Bruijn states by \(00,01,10,11\). A transition \((a,b)\to(b,c)\) is allowed exactly when \(a=c\ne b\) is false. Its transfer matrix is
\[
T=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
The trace \(\operatorname{tr}(T^k)\) counts labelled cyclic words of length \(k\) without singleton runs. Direct expansion gives
\[
\det(zI-T)=(z^2-z-1)(z^2-z+1).
\]
The first factor has roots \(\phi\) and \((1-\sqrt5)/2\), while the second has roots \(e^{\pm i\pi/3}\). Hence \(\operatorname{tr}(T^k)=L_k+2\cos(k\pi/3)=R_k\) for all positive \(k\), including every \(k\ge3\) required here.

**3. The temporal bipartite double cover.** For any graph \(G\), construct \(B(G)\) with vertices \((v,t)\), \(t\in\{0,1\}\), and edges \((u,0)\sim(v,1)\) whenever \(u\sim v\) in \(G\). A fixed majority configuration on \(B(G)\), with the two temporal-layer words \(x,y\), satisfies \(x=F_G(y)\) and \(y=F_G(x)\). Such a pair is uniquely determined by \(x\in\operatorname{Fix}(F_G^2)\), so
\[
q_G=\#\operatorname{Fix}(F_{B(G)}).
\]
If \(G\) is bipartite, \(B(G)\) is the disjoint union of two copies of \(G\). The prism \(P_n\) is bipartite exactly for even \(n\), and the Möbius ladder \(M_n\) is bipartite exactly for odd \(n\).

For odd \(n\), the cover \(B(P_n)\) is isomorphic to \(P_{2n}\): for a lifted prism vertex \((i,j,t)\), select the unique \(k\pmod{2n}\) satisfying \(k\equiv i\pmod n\) and \(k\equiv t\pmod2\). Horizontal edges change \(k\) by one and rung edges change \(k\) by \(n\) while swapping \(j\). Shifting the \(j=1\) rail coordinate by \(n\) produces standard prism rungs. For even \(n\), the cover \(B(M_n)\) is also isomorphic to \(P_{2n}\): write a lifted vertex as \((k,t)\), put \(s\equiv t+k\pmod2\), and map it to \(((k+ns)\bmod2n,s)\). Horizontal edges become unit rail edges and antipodal edges become standard rungs. Consequently
\[
B(P_n)\cong\begin{cases}P_n\sqcup P_n,&n\text{ even},\\P_{2n},&n\text{ odd},\end{cases}
\]
\[
B(M_n)\cong\begin{cases}P_{2n},&n\text{ even},\\M_n\sqcup M_n,&n\text{ odd}.\end{cases}
\]
Substituting the fixed-state counts from Step 1 proves the displayed formulas for \(q_P,q_M\). Removing the \(f_X\) fixed configurations and pairing the remaining two-step-returning configurations into orbits proves the formulas for \(b_P,b_M\).

**4. No longer recurrent periods.** The finite-graph period-two theorem for symmetric majority dynamics is classical, but a direct argument also applies. Write spins as \(x_t(v)\in\{-1,1\}\) and \(S_v(t)=\sum_{u\sim v}x_t(u)\), which is never zero on a cubic graph. The integer quantity \(H_t=\sum_v x_{t+1}(v)S_v(t)\) is bounded and, by symmetry of adjacency,
\[
H_t-H_{t-1}=\sum_v\bigl(x_{t+1}(v)-x_{t-1}(v)\bigr)S_v(t)\ge0.
\]
Each summand is strictly positive when its two spins differ, because \(x_{t+1}(v)=\operatorname{sgn}S_v(t)\). Thus \(H_t\) eventually stops increasing, forcing \(x_{t+1}=x_{t-1}\) thereafter. Every eventually recurrent configuration therefore has period one or two.

**5. Exact seam discrepancy.** Set \(c_n=2\cos(n\pi/3)\); its values by residue modulo six are \(2,1,-1,-2,-1,1\). The Lucas identity \(L_{2n}=L_n^2-2(-1)^n\), together with \(c_{2n}=c_n^2-2\), gives
\[
R_{2n}-R_n^2=-2c_nL_n-2(-1)^n-2.
\]
For odd \(n\), \(b_P-b_M=(R_{2n}-R_n^2)/2=-c_nL_n\). For even \(n\), \(b_P-b_M=(R_n^2+4R_n-R_{2n})/2=(c_n+2)L_n+2c_n+2\). These are exactly the four residue-dependent cases in the theorem. Since \(R_n=\phi^n+O(1)\), both primitive-orbit populations are asymptotic to \(\phi^{2n}/2\) and the seam discrepancy is of the smaller stated order.

## Verification

The companion standard-library Python program `verify_twist_majority.py` independently enumerates all \(2^{2n}\) labelled spin configurations of both graphs for each \(3\le n\le10\), counting fixed configurations and two-step returns from the actual microscopic neighbor-majority update. In total, it tests \(2{,}796{,}160\) labelled graph/configuration pairs. It also compares the cyclic-word count against a separate exhaustive binary-word test for \(3\le n\le15\), verifies the explicit temporal-cover graph isomorphisms for both families for \(3\le n\le30\), and checks the Lucas discrepancy identity for \(3\le n\le1000\). Run `python3 verify_twist_majority.py`; expected final line: `TWISTED_LADDER_MAJORITY_VERIFY_OK`. `verification_output.txt` records the actual successful run. These finite tests corroborate but do not replace the infinite-family proof above.

## Relationship to prior work

The established Goles--Olivos finite-graph theorem, as discussed explicitly by Tamuz--Tessler and Benjamini--Chan--O'Donnell--Tamuz--Tan, guarantees eventual period at most two, not exact orbit counts on the two ladder families. Agur's fixed-point analysis uses one-dimensional periodic majority neighborhoods, not the two-rail cubic graph with a twist. McSorley's 1998 paper counts structures of Möbius ladders; its abstract does not identify a synchronous majority orbit census, but a complete full-text comparison could not be completed. Existing formulae for majority dynamics on open ladders and leaf-decorated rings concern different graphs or boundary conditions and do not imply the signed prism-versus-Möbius seam discrepancy. The present claim is limited to exact counts and their comparison; it does not claim a new general period-two theorem or a new formula for all singleton-free cyclic words.

## Limitations

No basin-size, first-entry-time, or mixing-time distribution is asserted. The result counts labelled configurations and temporal orbits only, without taking quotient by graph automorphisms. The published-literature comparison is not exhaustive, and the inaccessible full text of McSorley's broadly relevant enumeration paper leaves a residual historical-equivalence risk. Independent validation has not been performed.

## References

1. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035 (first submitted July 15, 2013), especially Sections 1.1, 3.1, and 3.4. https://arxiv.org/abs/1307.4035
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (first submitted May 11, 2014), especially Introduction and Sections 2--3. https://arxiv.org/abs/1405.2486
3. Z. Agur, *Fixed Points of Majority Rule Cellular Automata with Application to Plasticity and Precision of the Immune System*, Complex Systems 5 (1991), 351--357. https://www.complex-systems.com/abstracts/v05_i03_a06/
4. J. P. McSorley, *Counting Structures in the Möbius Ladder*, Discrete Mathematics 184 (1998), 137--164. https://digitalcommons.mtu.edu/michigantech-p/7264/
5. Goles and Olivos, classical period-two theorem for finite symmetric majority dynamics, as cited and discussed in References 1--2.
