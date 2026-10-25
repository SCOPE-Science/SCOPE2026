# Dyadic obstruction and exact minimal-component classification of modular Thue–Morse integrals

## Finding
Let \(\theta(0)=01\), \(\theta(1)=10\), and let \(Y\) be the two-sided Thue–Morse subshift with shift \(\sigma\). For every integer \(q\ge2\), the two-block modular antiderivative extension
\[
F_q(y,z)=(\sigma y,z+y_0\pmod q),\qquad (y,z)\in Y\times\mathbb Z/q\mathbb Z,
\]
has exactly \(2^s\) clopen minimal components, where \(q=2^s m\) and \(m\) is odd. Each component is uniquely ergodic and conjugate to
\[
(y,r)\longmapsto (\sigma y,r+d\pmod m),\quad d=2^{-1}\pmod m,
\]
with the one-point group understood if \(m=1\). Thus \(F_q\) is minimal and uniquely ergodic precisely when \(q\) is odd.

The classification includes explicit continuous transfer functions. It also implies that for the one-sided Thue–Morse word \(t=t_0t_1\cdots\), the prefix sums \(S_n=\sum_{j=0}^{n-1}t_j\) are equidistributed among all \(q\) residues in natural density, including when \(F_q\) is nonminimal. The previously known case \(q=2\) is not a new claim.

## Assumptions and scope
The binary Thue–Morse subshift is the orbit closure of a bilateral substitution point whose nonnegative half is the fixed point \(t\) with \(t_0=0\), \(t_{2n}=t_n\), \(t_{2n+1}=1-t_n\). It is aperiodic, minimal and uniquely ergodic. Standard recognizability of the aperiodic primitive constant-length substitution gives a continuous dyadic-address factor \(\pi:Y\to\mathbb Z_2\) satisfying \(\pi(\sigma y)=\pi(y)+1\) and, for the chosen substitution-aligned point \(y^*\), \(\pi(y^*)=0\). The formulas below do not require a global continuous choice of a real phase: only the finite-level residues of \(\pi\) are used.

For each \(q\ge2\) write \(q=2^s m\) with \(m\) odd. An optional factor \(\mathbb Z/1\mathbb Z\) is trivial. The extension is also the shift on
\[
X_q=\{x\in(\mathbb Z/q\mathbb Z)^{\mathbb Z}:\ (x_{n+1}-x_n\pmod q)_{n\in\mathbb Z}\in Y\},
\]
where \(x\mapsto((x_{n+1}-x_n)_n,x_0)\) is the explicit conjugacy to \(F_q\).

## Proof
**1. The arithmetic identity and its continuous extension.** Substitution gives \(t_{2k}=t_k\) and \(t_{2k+1}=1-t_k\). Consequently
\[
S_{2k}=k,\qquad S_{2k+1}=k+t_k.
\]
Let \(r(y)\in\{0,1,\ldots,2^{s+1}-1\}\) denote \(\pi(y)\bmod 2^{s+1}\), and \(\epsilon(y)=r(y)\bmod2\). Set
\[
u_s(y)=\lfloor r(y)/2\rfloor+\epsilon(y)(1-y_0)\pmod{2^s}.
\]
For odd \(m>1\), put \(d=2^{-1}\pmod m\) and
\[
u_m(y)=\epsilon(y)(d-y_0)\pmod m.
\]
Both maps are continuous (they depend on finite odometer residues and a symbol). On the forward orbit of \(y^*\), the prefix-sum identity yields
\[
S_n\equiv u_s(\sigma^n y^*)-u_s(y^*)\pmod{2^s},
\quad S_n\equiv nd+u_m(\sigma^n y^*)-u_m(y^*)\pmod m.
\]
Here \(u_s(y^*)=u_m(y^*)=0\). For odd \(n=2k+1\), the second equality uses \(2d=1\pmod m\) and \(t_{2k+1}=1-t_k\). Taking successive differences and using density of this forward orbit, continuity proves for **every** \(y\in Y\):
\[
y_0=u_s(\sigma y)-u_s(y)\pmod{2^s},\qquad
y_0=d+u_m(\sigma y)-u_m(y)\pmod m.
\]
For \(s=0\) or \(m=1\), ignore the corresponding trivial factor.

**2. Exact topological conjugacy.** By the Chinese remainder theorem, define
\[
H(y,z)=(y,z-u_s(y)\pmod{2^s},z-u_m(y)\pmod m).
\]
It is a homeomorphism, and the two cohomology identities give
\[
H\circ F_q\circ H^{-1}(y,a,b)=(\sigma y,a,b+d).
\]
It remains to prove that \(T_m(y,b)=(\sigma y,b+d)\) on \(Y\times\mathbb Z/m\mathbb Z\) is minimal and uniquely ergodic for every odd \(m\).

**3. Odd cyclic rotations have no hidden components.** The constant-group skew product \(T_m\) is already conjugate by \((y,b)\mapsto(y,2b)\) to \(V_m(y,r)=(\sigma y,r+1)\), because \(2d=1\pmod m\). Define the length-two substitution on the \(2m\)-letter alphabet \(\{0,1\}\times\mathbb Z/m\mathbb Z\) by
\[
\Psi(a,r)=(a,2r)\,(1-a,2r+1).
\]
The one-sided fixed point beginning with \((0,0)\) is precisely \((t_n,n\bmod m)_{n\ge0}\). This substitution is primitive when \(m\) is odd. Indeed, for every residue \(r\pmod m\) there are indices of each Thue–Morse symbol in that residue: choose one index \(j\) in the residue; if \(o\) is the multiplicative order of \(2\) modulo \(m\), choose \(B\) larger than the binary length of \(j\) and put
\[
N=\sum_{i=0}^{m-1}2^{B+io}.
\]
Then \(N\equiv0\pmod m\), while its binary support is disjoint from \(j\) and consists of the odd number \(m\) of digits. Hence \(j+N\equiv j\pmod m\) but \(t_{j+N}=1-t_j\). (For \(m=1\), this argument reduces to the ordinary primitive Thue–Morse substitution.) In the block \(\Psi^k(a,r_0)\), position \(j\) carries letter \((t_j\oplus a,2^kr_0+j\bmod m)\); all \(2m\) letters appear once \(k\) is sufficiently large. Thus \(\Psi\) is primitive.

The substitution orbit is not a proper subshift of \(Y\times\mathbb Z/m\mathbb Z\). Let \(w\) be any allowed finite factor of \(Y\) and \(r\) any residue. Primitivity of \(\theta\) gives a sufficiently high \(k\) such that \(w\) occurs at a fixed offset \(j\) inside \(\theta^k(a)\) for some symbol \(a\). In the fixed word \(t\), this supertile occurs at every position \(2^k b\) with \(t_b=a\). As \(2^k\) is invertible modulo odd \(m\), the preceding equal-symbol-in-every-residue observation permits a choice of \(b\) with \(2^kb+j\equiv r\pmod m\). Therefore \(w\) occurs at positions representing every residue modulo \(m\). The orbit of \((t,0)\) in \(Y\times\mathbb Z/m\mathbb Z\) is dense. Because this orbit closure is exactly the primitive substitution subshift of \(\Psi\), it is minimal and uniquely ergodic. Hence \(V_m\), and thus \(T_m\), are strictly ergodic.

**4. Exhaustion of components and residue frequencies.** In conjugate coordinates, each value \(a\in\mathbb Z/2^s\mathbb Z\) gives a clopen invariant copy of the strictly ergodic \(T_m\); there can be no other minimal components. For residue frequencies, unique ergodicity of \(Y\times\mathbb Z/m\mathbb Z\) implies that \(t_k\) is uniformly distributed between its two symbols within each congruence class of \(k\pmod m\), because the invariant product measure is the (unique) measure and the Thue–Morse measure assigns each digit mass \(1/2\) by complement symmetry. For general \(q=2^s m\), writing \(k=2^su+r\) gives \(t_k=t_u\oplus t_r\), so the same fair conditional distribution holds within every residue class modulo \(q\). Among even indices \(n=2k\), the identity \(S_n=k\) yields density \(1/(2q)\) for each residue. Among odd indices \(n=2k+1\), \(S_n=k+t_k\); conditional fairness in each \(k\pmod q\) yields another \(1/(2q)\). Hence every residue of \(S_n\pmod q\) has natural density exactly \(1/q\).

## Verification
The standalone `verify.py` reconstructs the Thue–Morse prefix-sum and the two finite-level transfer identities for many moduli and indices, and independently checks the finite substitution-column identities and witnesses of all symbols in odd residue classes. Its finite checks support—but do not replace—the infinite arguments above.

## Relationship to prior work
Kang and Jäger, *Lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1, Theorem 1.7 and the paragraph immediately following, prove a strict-ergodicity criterion for lifts **of the period-doubling subshift** and observe nonminimality of the binary two-block lift of the Thue–Morse subshift. Their even/odd-length classification over the period-doubling base is not an all-modulus classification over the Thue–Morse base. Berthé and collaborators, *Density of group languages in shift spaces*, arXiv:2403.17892, Example 7.12, already exhibit the nonergodic two-component \(q=2\) skew product over Thue–Morse and equal residue densities; both facts are specifically attributed rather than presented as new. Earlier general results on primitive substitutions, recognizability and finite-group extensions are used as background. The additional uniform all-modulus conjugacy, precise \(2\)-primary component law and all-modulus residue-density assertion were not located in the inspected material; historical priority remains a live limitation.

## Limitations
Only the unweighted binary one-letter cocycle \(y\mapsto y_0\pmod q\) is treated, and the explicit splitting depends on the Thue–Morse substitution and its dyadic address. The result does not classify arbitrary permutative block codes, arbitrary cocycles or other substitutions. A finite verifier cannot certify the infinite theorem. The assessment of novelty is bounded by the inspected literature and records; independent mathematical audit and historical-priority assessment have not been performed.

## References
1. Z. Kang and T. Jäger, *Lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1 (first submitted 2026-09-01), https://arxiv.org/pdf/2609.01140.
2. V. Berthé et al., *Density of group languages in shift spaces*, arXiv:2403.17892, especially Example 7.12, https://arxiv.org/abs/2403.17892.
3. Standard Mossé recognizability theorem for primitive aperiodic substitutions; only its constant-length odometer-address consequence is used.
