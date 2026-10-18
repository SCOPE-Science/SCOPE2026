# Universal saturated socle fibers for finite local Gorenstein algebras

## Finding

Let \(k=\mathbb F_q\) and let \(R\) be a commutative, local, finite-dimensional \(k\)-algebra with residue field \(R/\mathfrak m=k\), dimension \(s\geq2\), and one-dimensional socle \(\operatorname{Ann}_R(\mathfrak m)=k\omega\). Fix \(r\geq1\), set \(n=sr\), and prescribe a matrix \(C\in M_n(k)\) with \(C^2=0\) and \(\operatorname{rank}C=r\).

**Theorem (fixed saturated socle fiber).** The set of unital \(k\)-algebra homomorphisms \(\rho:R\longrightarrow M_n(k)\) for which \(\rho(\omega)=C\) has cardinality

\[
\boxed{\#\{\rho:\rho(\omega)=C\}=q^{(s-2)r^2}\,|\operatorname{GL}_{(s-2)r}(k)|.}
\]

Here \(|\operatorname{GL}_0(k)|=1\). The count is independent of the algebra multiplication, embedding dimension, chosen nonzero socle generator, and similarity class of the target (the latter is uniquely determined by its rank). Every homomorphism in this fiber equips \(k^n\) with the free \(R\)-module structure \(R^r\). For **any** finite \(R\)-module \(M\), moreover,

\[
\operatorname{rank}_k(\omega:M\to M)\leq\frac{\dim_k M}{s};
\]

equality holds exactly when \(M\) is free over \(R\). Thus the fixed-fiber condition is the extremal socle-rank stratum.

## Assumptions and scope

All algebras are associative, commutative, unital and finite-dimensional over \(k\); homomorphisms preserve the unit and the specified \(k\)-algebra structure. The hypothesis that the socle has dimension one is the Artinian Gorenstein condition. Because \(s\geq2\), \(\omega\in\mathfrak m\), hence \(\omega\mathfrak m=0\) and \(\omega^2=0\). The residue-field equality \(R/\mathfrak m=k\) is essential in the stated finite-field formula. The parameter \(r\) may be any positive integer; no condition on the characteristic is imposed.

The theorem counts labeled matrix representations with **the exact prescribed output** \(C\), not conjugacy classes of representations. It says nothing about fibers at smaller socle rank, nor does it assert scheme-theoretic smoothness or reducedness of the representation variety.

## Proof

**1. Socle rank forces a free summand.** Let \(M\) be a finite \(R\)-module and put \(t=\operatorname{rank}_k(\omega|_M)\). Choose \(v_1,\ldots,v_t\in M\) so that \(\omega v_1,\ldots,\omega v_t\) are independent. Define the \(R\)-linear map

\[
\Phi:R^t\to M,\qquad (a_i)_i\mapsto\sum_{i=1}^t a_i v_i.
\]

The socle of \(R^t\) is \((k\omega)^t\), and \(\Phi\) is injective on it. Every nonzero submodule \(N\leq R^t\) meets this socle nontrivially: choose a nonzero element of \(N\) and multiply it by a product from the maximal ideal of maximal possible length that remains nonzero. Its product is killed by \(\mathfrak m\), hence lies in the socle. Therefore \(\ker\Phi=0\). Thus \(M\) contains \(R^t\) as a submodule, and \(\dim_k M\geq st\). If equality holds, \(\Phi\) is an isomorphism and \(M\cong R^t\). Conversely the linear map \(\omega\) on \(R^t\) has image \((k\omega)^t\) of dimension \(t\), so every free module attains equality.

**2. Saturated representations form one conjugacy orbit.** Let \(\lambda:R\to M_s(k)\) denote the left regular representation. On \(R^r\), the operator \(\lambda_r(\omega)\) has rank \(r\), and it squares to zero. By the lemma, every \(\rho\) with \(\operatorname{rank}\rho(\omega)=r\) yields a module isomorphic to \(R^r\). Hence these homomorphisms are exactly the \(\operatorname{GL}_n(k)\)-conjugates of \(\lambda_r\). Their stabilizer is \(\operatorname{Aut}_R(R^r)=\operatorname{GL}_r(R)\). Reduction modulo \(\mathfrak m\) gives a surjection \(\operatorname{GL}_r(R)\to\operatorname{GL}_r(k)\) with kernel \(1+M_r(\mathfrak m)\) of size \(q^{(s-1)r^2}\). Thus

\[
\#\{\rho:\operatorname{rank}\rho(\omega)=r\}
=\frac{|\operatorname{GL}_n(k)|}{|\operatorname{GL}_r(k)|q^{(s-1)r^2}}.
\]

**3. Number of possible targets.** Every square-zero \(n\)-by-\(n\) matrix of rank \(r\) is conjugate to \(C\), since its Jordan type is \((2^r,1^{n-2r})\), and \(n\geq2r\). Put \(h=n-2r=(s-2)r\). Relative to a decomposition \(k^n=E\oplus U\oplus F\), with dimensions \((r,h,r)\) and \(C:F\to E\) the identity, every matrix centralizing \(C\) is precisely of the form

\[
Z=\begin{pmatrix} A&B&D\\0&H&K\\0&0&A\end{pmatrix},
\]

where \(A\in M_r(k)\), \(H\in M_h(k)\), while \(B,D,K\) are unconstrained blocks of their indicated sizes. It is invertible exactly when \(A\) and \(H\) are invertible. Therefore

\[
|\operatorname{Cent}_{\operatorname{GL}_n(k)}(C)|
=|\operatorname{GL}_r(k)|\,|\operatorname{GL}_h(k)|q^{r^2+2rh}
=|\operatorname{GL}_r(k)|\,|\operatorname{GL}_h(k)|q^{(2s-3)r^2}.
\]

The number of rank-\(r\) square-zero target matrices is \(|\operatorname{GL}_n(k)|/|\operatorname{Cent}_{\operatorname{GL}_n(k)}(C)|\). Conjugation makes all fibers over these targets equipotent. Dividing the representation count in step 2 by this target count gives

\[
\frac{|\operatorname{Cent}_{\operatorname{GL}_n(k)}(C)|}{|\operatorname{GL}_r(R)|}
=q^{(s-2)r^2}|\operatorname{GL}_{(s-2)r}(k)|.
\]

This proves the exact formula and its universality.

## Verification

A standalone program, `verify_socle.py`, implements an independent bit-matrix enumeration over \(\mathbb F_2\). It exhaustively checks the prescribed rank-one target \(C\) for cubic and quartic powers in dimensions three and four, respectively, and all commuting square-zero pairs in dimension four. The observed fiber sizes are \(2\), \(24\), and \(24\), agreeing with the theorem. It also checks the orbit-stabilizer identity symbolically as integer arithmetic for six lengths and four field orders. The executable prints `VERIFY_OK_SOCLE_UNIVERSALITY` on success. These finite checks support but do not establish the arbitrary-algebra theorem; the proof above supplies the unrestricted argument.

For instance the nonisomorphic length-four Gorenstein algebras \(k[t]/(t^4)\) with \(\omega=t^3\) and \(k[x,y]/(x^2,y^2)\) with \(\omega=xy\) give the same number \(q^2|\operatorname{GL}_2(k)|\) of presentations of any rank-one square-zero \(C\in M_4(k)\). These two specializations are illustrations, not separately asserted priority claims.

## Relationship to prior work

Levy's work studies the representation varieties of the two-generator square-zero algebra and their geometry. Kokol Bukovšek–Košir–Novak–Oblak study products of commuting nilpotent operators, including rank constraints. Hua studies finite-field matrix polynomial equations. The present theorem is a cross-algebra fixed-output count in the saturated socle-rank locus: its scope ranges over every commutative local Artinian Gorenstein algebra with residue field \(k\), rather than one presentation or a single product pattern. The relevant free-module rigidity and centralizer calculation are proved here in full. The existence of a different formulation elsewhere in the literature has not been excluded.

## Limitations

The result does not classify nonsaturated fibers, non-Gorenstein local algebras, algebras with larger residue fields, or general noncommutative Frobenius algebras. Neither scheme-theoretic multiplicities nor a full classification of connected components is claimed. Verification is finite and not independent certification. Literature searches cannot establish absolute priority; equivalently formulated representation-variety orbit calculations might exist.

## References

1. P. Levy, *Varieties of Modules for \(\mathbb Z/2\mathbb Z\times\mathbb Z/2\mathbb Z\)*, arXiv:math/0609180 (first public version 6 September 2006). https://arxiv.org/abs/math/0609180
2. D. Kokol Bukovšek, T. Košir, B. Novak and P. Oblak, *Products of commuting nilpotent operators*, Electronic Journal of Linear Algebra **16** (2007), 237–247, doi:10.13001/1081-3810.1199.
3. J. Hua, *Polynomial equations for matrices over finite fields*, Bulletin of the Australian Mathematical Society **59** (1999), 59–64, doi:10.1017/S0004972700032603.
