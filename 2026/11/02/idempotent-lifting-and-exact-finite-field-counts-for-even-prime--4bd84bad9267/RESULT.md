# Idempotent lifting and exact finite-field counts for even prime dihedral quandles

## Finding

For an odd prime \(p\) and an odd prime power \(q\), let \(R_m\) denote the dihedral quandle on \(\mathbb Z/m\mathbb Z\) with \(i*j=2j-i\), and let \(I_m(q)\) count the elements \(x\) satisfying \(x^2=x\) in the quandle algebra \(\mathbb F_q[R_m]\), **including zero**. The canonical double-cover map \(R_{2p}\to R_p\) induces a surjective map on idempotent sets. The sizes of its fibers, and hence \(I_{2p}(q)\), are as follows.

Put
\[
L=\min\{j\ge1:2^j\equiv\pm1\pmod p\},\qquad
\epsilon\in\{1,-1\},\quad2^L\equiv\epsilon\pmod p,\qquad
N=2^L-\epsilon,\quad h=\frac{p-1}{2L}.
\]
If \(\operatorname{char}\mathbb F_q\ne p\), define \(H=\langle-1,2\rangle\le (\mathbb Z/p\mathbb Z)^\times\), let \(f\) be the order of the coset \(qH\) in \((\mathbb Z/p\mathbb Z)^\times/H\), and choose the **unique** signs and exponent
\[
\sigma\in\{1,-1\},\quad0\le a<L,\qquad q^f\equiv\sigma2^a\pmod p.
\]
Set \(d=\gcd(N,|q^f-\sigma2^a|)\). Then
\[
\boxed{I_{2p}(q)=(q+1)\bigl(1+dq^{Lf}\bigr)^{h/f}.}
\]
More precisely, an idempotent \(y\in\mathbb F_q[R_p]\) has augmentation \(b\in\{0,1\}\) and a uniquely determined number \(t\in\{0,\ldots,h/f\}\) of active Frobenius-orbits of \(H\)-cosets in its nonzero Fourier support. It has exactly \(q^{b+Lft}\) idempotent lifts to \(\mathbb F_q[R_{2p}]\). Each orbit independently has one inactive choice or \(d\) active choices.

If \(\operatorname{char}\mathbb F_q=p\), then
\[
\boxed{I_{2p}(q)=1+q^{\,h+(p+1)/2}.}
\]
In this modular case the zero idempotent has one lift, and every nonzero idempotent in \(\mathbb F_q[R_p]\) has exactly \(q^{(p+1)/2}\) lifts. The formulas apply to all odd prime powers \(q\), with no assumption that \(\mathbb F_q\) contains \(p\)-th roots of unity.

For example, \(I_6(3)=28\), \(I_6(5)=96\), \(I_{10}(3)=184\), \(I_{10}(5)=626\), and \(I_{14}(3)=760\). The modular and nonmodular regimes are genuinely different.

## Assumptions and scope

The algebra is a nonassociative \(\mathbb F_q\)-algebra with basis \(\{e_i:i\in\mathbb Z/m\mathbb Z\}\), and bilinear multiplication \(e_i e_j=e_{2j-i}\). The field order \(q\) is odd. The prime \(p\ge3\) is distinct from the coefficient characteristic only in the first formula; the second formula treats coefficient characteristic \(p\) explicitly. The quotient \(\pi:\mathbb F_q[R_{2p}]\to\mathbb F_q[R_p]\) sends \(e_i\mapsto e_{i\bmod p}\). Fourier support means the set of nonzero Fourier coefficients over a splitting extension, grouped into orbits under both \(\langle-1,2\rangle\) and the coefficient Frobenius; the number of active Frobenius-orbits is intrinsic.

## Proof

**1. A split double cover and a linear lifting problem.** Since the coefficient characteristic is odd, define
\[
s(e_j)=\frac12(e_j+e_{j+p})\quad(0\le j<p).
\]
Directly multiplying four basis terms shows \(s(e_i)s(e_j)=s(e_{2j-i})\), so \(s\) is an algebra section of \(\pi\). Its kernel \(W\), spanned by \(w_j=e_j-e_{j+p}\), is a right annihilator: \(A_{2p}W=0\). Therefore every element above an idempotent \(y\) has the unique form \(s(y)+w\), and
\[
(s(y)+w)^2=s(y)+w\,s(y).
\]
Thus its idempotent lifts form the vector space \(\ker(R_{s(y)}|_W-I)\).

Here and below multiplication of Laurent polynomials is ordinary **associative group-ring** multiplication, distinguished from the quandle product. Write \(C=\mathbb F_q[u]/(u^p-1)\), let \(\iota(u)=u^{-1}\) and \(D_2(u)=u^2\). Identifying a coefficient vector \(y=\sum_jy_j e_j\) with \(Y=\sum_jy_j u^j\), the quandle square equation is
\[
Y=\iota(Y)D_2(Y).\tag{1}
\]
Let \(c=(p+1)/2\), interpreted modulo \(p\), and identify \(W\) with \(C\) using \(w_i\mapsto(-1)^iu^{ci}\). This is consistent with \(w_{i+p}=-w_i\) because \(p\) is odd. Since \(w_i s(e_j)=w_{2j-i}\), the restricted right multiplication becomes
\[
T_Y:Z\longmapsto\iota(Z)Y.\tag{2}
\]
Consequently, the idempotent fiber over \(y\) is an \(\mathbb F_q\)-vector space of dimension \(\dim\ker(T_Y-I)\).

**2. The nonmodular Fourier classification.** Assume \(\operatorname{char}\mathbb F_q\ne p\). Over an algebraic closure containing all \(p\)-th roots of unity, let \(B_k\) be the evaluation of \(Y\) at the character indexed by \(k\in\mathbb Z/p\mathbb Z\). Equation (1) is equivalent to
\[
B_k=B_{-k}B_{2k}\qquad(k\in\mathbb Z/p\mathbb Z).\tag{3}
\]
At \(k=0\), \(B_0=b\in\{0,1\}\). At each nonzero pair \(\{k,-k\}\), (3) implies either both coefficients vanish, or both are nonzero and satisfy \(B_kB_{-k}=1\). Indeed \(B_k=B_{-k}B_{2k}\) and \(B_{-k}=B_kB_{-2k}\); a nonzero pair forces the product \(B_{2k}B_{-2k}=1\). The transformation \(k\mapsto2k\) permutes the nonzero pairs, so each \(H=\langle-1,2\rangle\)-coset is wholly inactive or wholly active.

In an active coset, choose a representative \(k\) and \(z=B_k\). Reciprocality and (3) give \(B_{-k}=z^{-1}\) and \(B_{2^jk}=z^{2^j}\). Closing the orbit at \(2^Lk=\epsilon k\) gives \(z^N=1\). Conversely any \(z\in\mu_N\) produces exactly one nonzero coefficient pattern on that coset. Since \(H\) has order \(2L\), there are \(h\) cosets.

An \(\mathbb F_q\)-rational coefficient vector is characterized by \(B_{qk}=B_k^q\). Frobenius acts on the \(h\) cosets in cycles of the same length \(f\); there are \(h/f\) cycles. Once an orbit is activated, its initial parameter \(z\) determines the other \(f-1\) parameters, and closing the cycle requires
\[
z^{q^f}=z^{\sigma2^a}.
\]
There are exactly \(d=\gcd(N,|q^f-\sigma2^a|)\) choices in the algebraic closure, including when the field characteristic divides \(N\): the displayed gcd is automatically coprime to the coefficient characteristic. Every Frobenius cycle therefore gives one inactive pattern or \(d\) active patterns.

**3. Nonmodular lift dimensions.** Fourier evaluation of (2) gives
\[
Z_k=Z_{-k}B_k.\tag{4}
\]
At frequency zero this has a free parameter exactly when \(b=1\). At an inactive pair \(\{k,-k\}\), both variables vanish; at an active pair, reciprocality \(B_kB_{-k}=1\) makes (4) a one-dimensional linear subspace. An active Frobenius cycle consists of \(Lf\) such pairs. The solution subspace of (4) is defined over \(\mathbb F_q\), so its \(\mathbb F_q\)-dimension equals its dimension after scalar extension (equivalently, finite-field Galois descent). It follows that the fiber dimension over a base idempotent with augmentation \(b\) and \(t\) active Frobenius cycles is exactly \(b+Lft\). Sum \(q^{b+Lft}\) over \(b\in\{0,1\}\) and the independent orbit choices to obtain
\[
\sum_{b=0}^{1}q^b\sum_{t=0}^{h/f}\binom{h/f}{t}d^t q^{Lft}
=(1+q)(1+dq^{Lf})^{h/f}.
\]

**4. Modular base idempotents.** Now \(\operatorname{char}\mathbb F_q=p\). The group algebra \(C\) is the local ring \(\mathbb F_q[u]/((u-1)^p)\), whose nilpotent maximal ideal is \(J=(u-1)\). If \(Y\) satisfies (1) and has augmentation zero, the \(J\)-adic leading order of its right side is at least twice that of its left side, since \(\iota\) and \(D_2\) preserve the filtration. Thus \(Y=0\). Every other idempotent has augmentation one and is a unit.

Put \(z=\log u\in J\) and write a unit of augmentation one as \(Y=\exp(F(z))\), using truncated formal logarithms/exponentials of degrees at most \(p-1\). All denominators used are invertible. Since \(\iota(z)=-z\) and \(D_2(z)=2z\), equation (1) is equivalent to
\[
F(z)=F(-z)+F(2z).
\]
An even-degree coefficient must vanish; an odd-degree coefficient at degree \(j\) is free exactly when \(2^{j-1}\equiv1\pmod p\). Exactly \(h=(p-1)/(2L)\) degrees \(1\le j<p\) have that property. Hence the base \(\mathbb F_q[R_p]\) has precisely \(1+q^h\) idempotents: zero and \(q^h\) augmentation-one units.

**5. Modular lift dimensions.** For every unit \(Y\) satisfying (1), applying \(\iota\) to (1) and multiplying the two resulting identities yields
\[
Y\iota(Y)=Y\iota(Y)D_2(Y\iota(Y)).
\]
Cancelling the unit and using invertibility of \(D_2\) gives \(Y\iota(Y)=1\). The element \(U=(1+Y)/2\) is a unit because it has augmentation one, and \(U/\iota(U)=Y\). Therefore
\[
T_Y(Z)=U\,\iota(Z/U),
\]
so \(T_Y\) is conjugate to \(\iota\). On the \(p\)-dimensional group ring, \(\iota\) fixes one basis element and exchanges \((p-1)/2\) pairs. Since the characteristic is odd, its \(+1\) eigenspace has dimension \((p+1)/2\). Each nonzero base idempotent therefore has \(q^{(p+1)/2}\) lifts; zero has only the zero lift. This yields \(1+q^{h+(p+1)/2}\) and completes the proof.

## Verification

The standalone source file `verify.cpp` enumerates all coefficient vectors directly in the prescribed nonassociative algebra and tests \(x^2=x\) without Fourier transforms or quotient arguments. Compile with `c++ -O3 -std=c++17 verify.cpp -o verify` and run `./verify`. It returned `VERIFY_OK` with the exact counts \((p,q,I_{2p}(q))\) equal to \((3,3,28)\), \((3,5,96)\), \((3,7,176)\), \((5,3,184)\), \((5,5,626)\), and \((7,3,760)\). The \(p=7,q=3\) run examines all \(3^{14}=4,782,969\) coefficient vectors; the other runs are smaller. The computation is independent corroboration, not a proof for unbounded primes or field sizes.

## Relationship to prior work

The quandle algebra and integral idempotent problem are developed by Sangare–Ta (2026). Elhamdadi–Ta–Virgin (2026) establishes the Fourier framework and addresses **integral** idempotents of Takasaki quandles, emphasizing odd-order latin cases. Kaur–Singh (2026) also studies integral odd-order latin dihedral idempotents, while Zhang (2026) treats Alexander quandle group-ring methods, integral augmentation filtrations, and odd-order Peirce spectra. The present theorem uses the known Fourier equation as a starting point but determines **finite-field idempotent fibers under the nonlatin double cover**, an exact nonmodular orbit product, and the modular jump. Previously available odd-prime \(R_p\) enumeration is not claimed as new; it does not provide the doubling-cover eigenspaces or the even-order counts by itself.

## Limitations

The coefficient field is finite of odd cardinality. Neither arbitrary coefficient rings nor characteristic two are covered. The dihedral quandle order is exactly twice an odd prime; general even composite orders require additional orbit analysis. The claim does not assert historical uniqueness, priority against inaccessible literature, or a result for the integral quandle ring. The smallest modular and nonmodular cases have independent exhaustive tests, but no computer enumeration verifies the theorem for all parameters.

## References

- B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550, first public posting 2026-08-03.
- D. Kaur and P. Singh, *A note on idempotents in quandle rings*, arXiv:2609.09183, first public posting 2026-08-29.
- M. Elhamdadi, L. Ta, and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799, first public posting 2026-09-03.
- Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204, first public posting 2026-10-06.
