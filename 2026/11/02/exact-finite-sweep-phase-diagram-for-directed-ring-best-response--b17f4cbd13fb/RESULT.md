# Exact finite-sweep phase diagram for directed-ring best responses

## Finding

**Theorem (all gains, all starting profiles).** Consider a directed cycle of \(n\ge3\) players, numbered cyclically, whose unique best-response functions are
\[
 x_i\longleftarrow F_i(x_{i-1}),\qquad
 F_i(z)=\max\{0,t_i-w_i z\},\qquad
 0<t_i<u_i,\quad w_i>0,\quad x_i\in[0,u_i],
\]
where \(x_0=x_n\). Players update in the fixed repeated order \(1,2,\ldots,n\), each making one exact best response per sweep. Set \(W=\prod_{i=1}^n w_i\). The following phase diagram holds for every starting action profile:

1. If \(0<W<1\), all full-sweep profiles converge geometrically to the **unique** Nash equilibrium.
2. If \(W=1\) and \(n\) is even, every trajectory becomes exactly constant at a Nash equilibrium after finitely many sweeps. The equilibrium set may be a continuum. If \(W=1\) and \(n\) is odd, every full-sweep trajectory becomes exactly periodic with period at most two after at most two sweeps; genuine two-cycles can occur.
3. If \(W>1\) and \(n\) is even, every trajectory becomes exactly constant at a Nash equilibrium after finitely many sweeps, and there are at most three Nash equilibria. If \(W>1\) and \(n\) is odd, every trajectory becomes exactly periodic with period at most two after finitely many sweeps, and there is at most one primitive period-two orbit (up to phase).

All assertions are constructive. Define \(L_0=0\), \(H_0=u_n\), \(B_0=0\), \(S_0=1\), and, for \(i=1,\ldots,n\),
\[
\begin{aligned}
 L_i&=\max\{0,t_i-w_iH_{i-1}\},&
 H_i&=\max\{0,t_i-w_iL_{i-1}\},\\
 B_i&=t_i-w_iB_{i-1},&
 S_i&=-w_iS_{i-1}.
\end{aligned}
\]
Writing \(L=L_n\), \(H=H_n\), \(B=B_n\), and \(S=(-1)^nW\), the entire full-sweep dynamics reduce exactly to
\[
\boxed{\quad z_{k+1}=T(z_k)
  =\operatorname{clip}(B+S z_k;L,H),\quad
 \operatorname{clip}(v;a,b)=\max\{a,\min\{v,b\}\}.\quad}
\]
Every full-sweep vector is reconstructed successively as \((F_1(z),F_2(F_1(z)),\ldots,T(z))\). Thus the scalar map yields the complete dynamics, not just a necessary bound.

For the homogeneous family \(u_i=2\), \(t_i=1\), \(w_i=2\), it yields
\[
T_3(z)=\operatorname{clip}(3-8z;0,1),\qquad
T_4(z)=\operatorname{clip}(-5+16z;0,1).
\]
The three-player game has one Nash equilibrium at scalar coordinate \(1/3\) and an attracting two-cycle \(0\leftrightarrow1\). The four-player game has three Nash equilibria at scalar coordinates \(0,1/3,1\), and every other initial scalar coordinate is absorbed into \(0\) or \(1\) in finitely many sweeps. At the critical weights \(w_i=1\), the corresponding maps are \(T_3(z)=\operatorname{clip}(1-z;0,1)\) and \(T_4(z)=\operatorname{clip}(z;0,1)\), exhibiting a continuum of two-cycles and a continuum of Nash equilibria, respectively.

## Assumptions and scope

The theorem concerns the one-predecessor directed cycle and one fixed, fair, cyclic update order, **not** arbitrary asynchronous revision orders or best-response-approaching rather than exact moves. The strategy caps \(u_i\) are finite and \(t_i<u_i\), making the upper clipping inactive for best replies. Such responses arise from utilities \(f_i(x_i+w_ix_{i-1})-c_i x_i\) when \(f_i\) is differentiable, strictly concave, increasing, and \(f_i'(t_i)=c_i>0\), with a uniquely maximizing target \(t_i\). These conditions ensure a well-defined, unique best response at every admissible profile. A Nash equilibrium is a simultaneous fixed point of all responses. A full sweep means exactly \(n\) successive unilateral updates in the specified order; periodicity is measured at sweep boundaries.

## Proof

**1. Scalar reduction and saturation closure.** For each input \(z\in[0,u_n]\), after one sweep player \(i\)'s action is \(G_i(z)=F_i\circ\cdots\circ F_1(z)\). Inductively, \(G_0(z)=z=\operatorname{clip}(z;0,u_n)\). The elementary identity
\[
 \max\{0,t-w\operatorname{clip}(v;a,b)\}
 =\operatorname{clip}(t-wv;\max\{0,t-wb\},\max\{0,t-wa\})
\]
holds for \(w>0\) and \(a\le b\). It proves \(G_i(z)=\operatorname{clip}(B_i+S_i z;L_i,H_i)\), with the displayed recursions. Since \(S_n=(-1)^nW\) and \(0\le L\le H\le t_n<u_n\), the return map is a self-map of \([0,u_n]\). Each Nash equilibrium corresponds bijectively to a fixed point of \(T\), by reconstructing all other coordinates.

**2. Contractive regime.** Each \(F_i\) is \(w_i\)-Lipschitz, so \(T\) is \(W\)-Lipschitz. If \(W<1\), the contraction theorem gives a unique fixed scalar, geometrically attracting all starting values. Reconstruction gives the unique Nash equilibrium and convergence of full profiles.

**3. Exact finite-settling lemma.** Let \(G(z)=\operatorname{clip}(b+az;p,q)\) have \(a>1\), \(p\le q\), and map its admissible interval into itself. After one iterate all values are in \([p,q]\). If \(p=q\), the assertion is immediate. Otherwise put \(r=-b/(a-1)\). For every \(z\in[p,q]\) strictly below \(r\), one has \(G(z)\le z\); until the lower clipping plateau is reached, the distance \(r-z\) is multiplied by \(a\) at each step. Hence the lower plateau is reached in finite time and is then fixed. The symmetric argument applies above \(r\), reaching the upper fixed plateau. The exceptional point \(z=r\), when admissible, is itself fixed. Therefore **every orbit becomes exactly stationary in finite time**, and all fixed points belong to \(\{p,q,r\}\) (after removing duplicates and inadmissible values). The argument also covers \(r\notin[p,q]\).

**4. Even cycle.** Here \(S=W>0\). When \(W>1\), apply the lemma directly to \(T\). When \(W=1\), \(T(z)=\operatorname{clip}(z+B;L,H)\). If \(B>0\), each nonstationary iterate within \([L,H]\) increases by \(B\) until it hits the upper plateau \(H\), which is fixed. If \(B<0\), the symmetric conclusion holds at \(L\). If \(B=0\), \(T\) is projection onto \([L,H]\), and all states reached after one sweep are Nash equilibria. This proves both even-cycle cases.

**5. Odd cycle.** Here \(S=-W<0\). Since \(T\) is nonincreasing, its fixed point is unique. Put \(p=T(H)\) and \(q=T(L)\), so \(p\le q\). Applying the same clipping identity gives the exact second-return map
\[
 T^2(z)=\operatorname{clip}\bigl((1-W)B+W^2z;p,q\bigr).
\]
When \(W=1\), this is the projection of \(z\) onto \([p,q]\), so \(T^2(T^2(z))=T^2(z)\): every orbit has become a fixed point of the second-return map after two sweeps, and hence is fixed or period two under \(T\). When \(W>1\), the finite-settling lemma applies to \(T^2\), proving finite entry to period at most two. The map \(T^2\) has at most three fixed points. The unique fixed point of \(T\) occupies one, while the other fixed points of \(T^2\), if present, are exchanged by \(T\). Therefore at most one primitive period-two orbit exists.

**6. Sharp boundary examples.** The homogeneous maps in the finding follow by the scalar coefficient recursions. Their directly computed fixed points and endpoint cycles prove that the parity and gain boundaries are realized, rather than artifacts of proof technique.

## Verification

Run `python3 VERIFY.py` with Python 3 and no third-party dependencies. Deterministic exact-rational checks confirm 53,550 direct-versus-clipped composition evaluations on heterogeneous rings, 510 unit-product identities, 6,480 supercritical finite-orbit samples, and four exact benchmark coefficient sets. The executable checks all produced profiles against the independently evaluated individual best responses using `fractions.Fraction`, avoiding floating-point threshold ambiguity. These finite checks test the implementation and illuminate boundary cases; they do not establish the all-size theorem, which follows from the preceding identities and finite-settling lemma.

## Relationship to prior work

Bayer, Kozics and Szőke [1,2] study best-response convergence and cycling in directed local-public-goods games. Their directed-cycle Example 3.2 shows an oscillating binary trajectory and notes even/odd differences, while their Example 5.1 and Theorem 5.5 provide convergence in a weak-influence/spectral-radius regime. Our subcritical convergence clause is consistent with and covered in spirit by their general theorem. The distinct contribution here is the **complete exact-return-map classification for fixed cyclic updates**, including arbitrarily heterogeneous weights and targets, both gain boundaries, finite-time stabilization in the supercritical even-ring regime, and the uniqueness of a possible supercritical odd-ring two-cycle. Their cited theorems do not imply these stronger-gain conclusions. General monotone-iteration convergence results, such as Olszewski [3], also do not by themselves imply finite-time plateau capture or the negative-orientation two-cycle classification.

## Limitations

The result is specific to exact full best-response sweeps on a directed one-predecessor cycle with positive substitutability weights, interior targets and a repeated consistent update order. Arbitrary update schedules, two-sided connections, noisy or partial adjustments, negative weights and unbounded action/target regimes are not included. The finite-settling time need not be uniformly bounded in the parameters: it diverges near the unit-gain boundary for carefully chosen initial conditions. Priority relative to any unlocated specialized clipped-map or cyclic-game treatment remains a residual literature risk. No claim of independent external validation is made.

## References

[1] P. Bayer, G. Kozics and N. G. Szőke, *Best-Response Dynamics in Directed Network Games*, Central European University Working Paper 2020_1, first public listing dated 2020-01-13. https://econpapers.repec.org/paper/ceueconwp/2020_5f1.htm

[2] P. Bayer, G. Kozics and N. G. Szőke, *Best-response dynamics in directed network games*, arXiv:2101.03863, initial arXiv version 2021-01-11; full accessible text, especially Sections 2, 3 and 5. https://arxiv.org/abs/2101.03863

[3] W. Olszewski, *A Result on Convergence of Sequences of Iterations with Applications to Best-Response Dynamics*, Mathematics of Operations Research 47 (2022), 2333–2343, online 2021-12-28. https://doi.org/10.1287/moor.2021.1210
