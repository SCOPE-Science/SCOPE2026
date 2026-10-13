# Lucas-number two-rank in a Mersenne cyclic-dihedral curve family

## Finding

Let \(K\) be an algebraically closed field of characteristic \(2\). For every odd integer \(r\geq 3\), set \(k=2^r-1\), and let \(C_r\) be the smooth projective curve with function field
\[
 K(C_r)=K(x,y),\qquad y^k=x^3+x^{-3}.
\]
Write \(\gamma(C_r)\) for the \(2\)-rank of its Jacobian, namely the integer for which \(J(C_r)[2](K)\cong (\mathbf Z/2\mathbf Z)^{\gamma(C_r)}\). Let \(L_0=2\), \(L_1=1\), and \(L_{r+2}=L_{r+1}+L_r\) be the Lucas numbers. Then
\[
\boxed{\gamma(C_r)=2(L_r-1).}
\]
The genus is \(g(C_r)=3(2^r-2)/2\). In particular, the exact \(2\)-ranks for \(r=3,5,7,9\) are respectively \(6,20,56,150\), against genera \(9,45,189,765\).

## Assumptions and scope

The base field is algebraically closed of characteristic \(2\); the parameter \(r\) ranges through all odd integers at least \(3\). Then \(k\) is odd and coprime to \(3\), so the displayed Kummer extension is separable and its unique smooth projective model is well defined. The invariant is geometric \(2\)-rank, not the rank of just one Cartier-matrix iterate. The formula is an equality for every permitted \(r\), and no assertion is made for even \(r\) (when \(3\mid 2^r-1\)).

## Proof

**1. Reduction by the involution.** The involution \(\iota:(x,y)\mapsto(x^{-1},y)\) has invariant \(u=x+x^{-1}\). In characteristic \(2\), \(x^3+x^{-3}=u^3+u=u(u+1)^2\). Its quotient is the smooth projective curve
\[
 E_k:\qquad z^k=u(u+1)^2.
\]
Timpanella's Proposition 4.6, or the Deuring–Shafarevich formula for this degree-two quotient with one fixed point, gives
\[
\gamma(C_r)=2\gamma(E_k).
\]
The Kummer cover \(E_k\to\mathbf P^1_u\) is totally ramified over exactly \(u=0,1,\infty\), with local exponents \(1,2,-3\) and genus \(g(E_k)=(k-1)/2\) by Riemann–Hurwitz. Indeed \(3\nmid k\), so all three ramification indices equal \(k\).

**2. A complete differential basis.** Define the integer set
\[
 I_k=\{j\in\{1,\ldots,k-1\}:\ k/3<j<k/2\}\ \cup\
     \{j\in\{1,\ldots,k-1\}:\ 2k/3<j<k\}.
\]
For \(j\in I_k\), let \(v_j=0\) in the first interval and \(v_j=1\) in the second. The differentials
\[
 \omega_j=(u+1)^{v_j}\frac{du}{z^j}\qquad(j\in I_k)
\]
are holomorphic. To see this directly, at the unique points above \(0,1,\infty\), the valuations of \(\omega_j\), respectively, are
\[
 k-1-j,\qquad k-1+kv_j-2j,\qquad -k-1-kv_j+3j.
\]
They are all nonnegative precisely for the two displayed ranges of \(j\) with their indicated \(v_j\). At unramified points the differentials have no poles. The \(\omega_j\) lie in distinct eigenspaces for the tame action \(z\mapsto\zeta z\), hence are linearly independent. Their number is \((k-1)/2=g(E_k)\), so they are a basis of \(H^0(E_k,\Omega^1)\).

**3. Exact Cartier action.** In characteristic \(2\), the Cartier operator \(\mathcal C\) satisfies \(\mathcal C(f^2\,du)=0\) and \(\mathcal C(f^2u\,du)=f\,du\). Its action on the above basis is
\[
\mathcal C(\omega_j)=
\begin{cases}
0,&j\text{ even and }v_j=0,\\
\omega_{j/2},&j\text{ even and }v_j=1,\\
\omega_{(j+k)/2},&j\text{ odd}.
\end{cases}
\]
For even \(j\), this follows by factoring out the square \(z^{-j}\). For odd \(j\), put \(m=(j+k)/2\) and use \(z^k=u(u+1)^2\) to write
\[
 \omega_j=\left(\frac{u+1}{z^m}\right)^2u(u+1)^{v_j}\,du.
\]
Both \(\mathcal C(u\,du)=du\) and \(\mathcal C(u(u+1)\,du)=du\), so \(\mathcal C(\omega_j)=(u+1)du/z^m=\omega_m\). In the two nonzero cases, the claimed target lies in \(I_k\) with the required value of \(v\). Thus the Cartier matrix is a partial permutation matrix: each nonzero arrow maps \(j\) to the residue \(2^{-1}j\pmod k\). In this functional graph, the stable Cartier rank is exactly the number of \(j\in I_k\) whose entire multiplicative-doubling orbit modulo \(k\) remains inside \(I_k\). The stable Cartier rank equals the geometric \(2\)-rank of the curve, while the rank of a single Cartier iterate need not do so.

**4. Binary necklace classification.** For \(k=2^r-1\), represent every residue \(1\le j<k\) by its \(r\)-digit binary word \(w_j\), with leading zeros allowed. Multiplication by \(2\) modulo \(k\) rotates the \(r\) digits cyclically. Moreover, the rational number \(j/k\) has repeating binary expansion \(0.\overline{w_j}_2\).

We claim that all rotations of \(w_j\) represent elements of \(I_k\) if and only if the *cyclic* word contains no adjacent pair of zero digits. If such a pair exists, rotate it to the front: then \(j/k<1/4<1/3\), so the rotation is outside \(I_k\). Conversely suppose no adjacent zeros occur. A rotation beginning in \(01\) represents a fraction strictly between \(1/3=0.\overline{01}_2\) and \(1/2\); one beginning in \(10\) represents a fraction strictly between \(2/3=0.\overline{10}_2\) and \(1\); and a rotation beginning in \(11\) is also above \(2/3\). The comparisons are strict because an odd-period word cannot be perfectly alternating. These possibilities exhaust rotations of a no-adjacent-zeros word. Hence such rotations lie in the two intervals defining \(I_k\).

There are \(L_r\) binary words on a labeled cycle of length \(r\) with no cyclically adjacent zeros: the adjacency matrix for allowed transitions \(1\to1\), \(1\to0\), \(0\to1\) is \(\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\), whose \(r\)-th power has trace \(L_r\). We must discard the all-ones word, since it represents the residue \(k\equiv0\pmod k\) rather than one of \(1,\ldots,k-1\). The all-zeros word is forbidden. Therefore
\[
 \gamma(E_k)=L_r-1,\qquad\gamma(C_r)=2(L_r-1),
\]
which proves the theorem.

## Verification

The included standalone program `verify.py` performs exact integer-arithmetic consistency checks for each odd \(r\) from \(3\) through \(15\). It constructs the basis intervals independently, tests the three valuations, reconstructs the Cartier transitions, iterates the transition graph to stable rank, compares complete modular-doubling orbits with the no-adjacent-zeros binary criterion, and checks the Lucas recurrence. It returns `VERIFY_OK` and the exact ranks \(6,20,56,150,396,1040,2726\). Run with `python verify.py`. The universal proof above does not rely on these finite checks.

## Relationship to prior work

Timpanella introduces the smooth curves \(y^k=x^M+x^{-M}\), proves their genus and cyclic-dihedral symmetry, and obtains the quotient formula \(\gamma(C)=2\gamma(C/\langle\iota\rangle)\) with a nonordinary upper bound (Proposition 4.6). That result does **not** evaluate the quotient \(2\)-rank for the Mersenne parameters here; the new evaluation supplies a closed Lucas-number expression rather than the known inequality. General tools for \(p\)-ranks of cyclic covers, including the Fermat-type formulas of Borges and Gonçalves, provide relevant context and possible alternative methods. They do not state this family-specific, exact Lucas-number specialization in the material inspected. The proof gives a direct Cartier calculation, independent of any asserted novelty of the quotient equation, Deuring–Shafarevich formula, or standard binary-string enumeration.

## Limitations

The theorem covers the \(M=3\) subfamily with Mersenne degree \(2^r-1\) and \(r\) odd. It does not determine the full \(2\)-torsion group scheme, the \(a\)-number, the Newton polygon, the zeta function, or \(2\)-ranks for other \(M\) or arbitrary \(k\). The Cartier transition description follows from elementary identities, but historical literature on three-point Kummer covers may contain an equivalent implicit computation; this remains a bibliographic risk. No independent mathematical audit has been performed.

## References

1. Marco Timpanella, *Large cyclic automorphism groups and cyclic subgroups of index two in characteristic two*, arXiv:2609.34709v1 (first public 2026-09-28), particularly Theorem 1.2 and Proposition 4.6. https://arxiv.org/pdf/2609.34709
2. Herivelto Borges and Cirilo Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987v3, particularly Sections 1–3 and 6. https://arxiv.org/pdf/2212.03987
3. I. Bouw, *The p-rank of ramified covers of curves*, Compositio Mathematica 126 (2001), 295–322, on general bounds and cyclic-cover methods.
