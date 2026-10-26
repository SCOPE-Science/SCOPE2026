# Ideal-product universality and a two-to-three threshold in finite Loewy-three Gorenstein rings

## Finding

Let \(R\) be a finite commutative local ring with maximal ideal \(\mathfrak m\) and residue field \(\mathbb F_q\). Suppose \(\mathfrak m^3=0\ne\mathfrak m^2\), that \(\dim_{\mathbb F_q}\mathfrak m^2=1\), and that multiplication induces a nondegenerate symmetric bilinear pairing on \(V=\mathfrak m/\mathfrak m^2\). Write \(r=\dim_{\mathbb F_q}V\ge2\). The nondegeneracy condition is equivalent to \(\operatorname{Soc}(R)=\mathfrak m^2\), i.e. to the Artinian Gorenstein property in this Loewy-three setting.

For \(s\ge0\), put
\[
 T_s(q)=\sum_{j=0}^s {s\brack j}_q,\qquad
 C_r(q)=\sum_{d=0}^r {r\brack d}_q T_{r-d}(q),\qquad N_r(q)=T_r(q)+2,
\]
where \({s\brack j}_q\) is the Gaussian binomial coefficient, the number of \(j\)-dimensional subspaces of \(\mathbb F_q^s\). For every integer \(k\ge1\), the ideal zero-product probability is
\[
 \boxed{\zeta_k(R)=1-\frac{1+kT_r(q)+\binom{k}{2}\bigl(T_r(q)^2-C_r(q)\bigr)}{N_r(q)^k}.}
\]
In particular this complete sequence depends **only** on \(q\) and \(r\): it is independent of the bilinear form's congruence class, the characteristic, and whether the finite local ring contains a coefficient field.

More precisely, write \(J_U\) for the inverse image of a subspace \(U\le V\) in \(\mathfrak m\). The entire distribution of the product of \(k\) independent uniform ideals is: product \(R\) with numerator \(1\); product \(J_U\) for each fixed nonzero \(U\) with numerator \(k\); product \(\mathfrak m^2=J_{\{0\}}\) with numerator \(k+\binom{k}{2}(T_r^2-C_r)\); and product zero with the remaining numerator. In every case the denominator is \(N_r^k\).

For fixed \(r\ge2\), along any sequence of finite fields whose orders \(q\to\infty\),
\[
 \boxed{\zeta_2(R)\longrightarrow0,\qquad
 \zeta_k(R)\longrightarrow1\quad\text{for every fixed }k\ge3.}
\]
At embedding dimension two, \(T_2=q+3\), \(C_2=3q+6\), and \(\zeta_2=5(q+3)/(q+5)^2\). This is an exact field-size dependence at fixed Loewy length three, contrasting with the chain-ring universality for which \(\zeta_2=5/8\).

## Assumptions and scope

All rings are finite commutative unital local rings. The integer \(r\ge2\) is fixed in the limiting statement, while \(q\) varies over prime powers; the individual rings need not belong to any one isomorphism class or characteristic. The assumptions permit different nondegenerate symmetric forms, including alternating forms in characteristic two. They exclude radical-square-zero rings, socles of dimension greater than one, and degenerate multiplication pairings. The invariant \(\zeta_k\), introduced in [1], samples ordered \(k\)-tuples from the **entire** ideal set, including \(0\) and \(R\), uniformly and independently.

## Proof

**1. The complete ideal lattice.** Multiplication induces \(B:V\times V\to\mathfrak m^2\), since \(\mathfrak m^3=0\). Both \(V\) and \(\mathfrak m^2\) are vector spaces over the residue field. Choose any identification of the one-dimensional target with \(\mathbb F_q\); only orthogonality, not this choice, matters. If \(I\subseteq\mathfrak m\) is a nonzero ideal not contained in \(\mathfrak m^2\), take \(x\in I\setminus\mathfrak m^2\). Nondegeneracy provides \(y\in\mathfrak m\) with \(B(\bar x,\bar y)\ne0\). Thus \(0\ne xy\in I\cap\mathfrak m^2\), forcing \(\mathfrak m^2\subseteq I\), because \(\dim_{\mathbb F_q}\mathfrak m^2=1\). If \(I\subseteq\mathfrak m^2\), it is either zero or \(\mathfrak m^2\). Every proper nonzero ideal therefore contains \(\mathfrak m^2\). Conversely, every inverse image \(J_U\) of a subspace \(U\le V\) is an ideal: multiplication by any element of \(R\) acts on \(V\) as multiplication by its residue scalar, and its other contributions lie in \(\mathfrak m^2\). Hence the ideal set is precisely \(\{0,R\}\cup\{J_U:U\le V\}\), with \(N_r=T_r+2\) elements.

**2. Orthogonal product test.** For any subspaces \(U,W\le V\), the product \(J_UJ_W\) lies in the one-dimensional ideal \(\mathfrak m^2\). It equals zero exactly if \(B(U,W)=0\), equivalently \(W\le U^{\perp_B}\); otherwise it equals \(\mathfrak m^2\). For every fixed \(d\)-dimensional \(U\), nondegeneracy gives \(\dim U^{\perp_B}=r-d\), independent of the form's isometry type. There are \({r\brack d}_q\) choices of \(U\) and \(T_{r-d}\) choices of \(W\). Thus precisely \(C_r\) of the \(T_r^2\) ordered pairs of proper nonzero ideals have zero product.

**3. Complete \(k\)-factor law.** Any tuple containing the zero ideal has zero product. Otherwise the identity ideal \(R\) may be discarded. If the tuple has no other proper factor, its product is \(R\). If it has exactly one proper factor, its product is that \(J_U\). If it has exactly two proper factors, Step 2 says that the product is zero in \(C_r\) ordered pairs of choices and equals \(\mathfrak m^2\) in \(T_r^2-C_r\) choices. If it has at least three proper factors, its product is zero because \(\mathfrak m^3=0\). The nonzero outcomes therefore have counts \(1\), \(k\) per \(J_U\ne\mathfrak m^2\), and \(k+\binom{k}{2}(T_r^2-C_r)\) for \(\mathfrak m^2\). Summing proves the displayed probability formula and complete product distribution, also for the boundary case \(k=1\).

**4. Large-field threshold.** For fixed \(r\), the Gaussian coefficient \({r\brack d}_q\) is a polynomial of degree \(d(r-d)\) with positive leading coefficient. Thus \(T_r(q)\asymp q^{\lfloor r^2/4\rfloor}\). Likewise each summand in \(C_r\) has degree at most \(d(r-d)+\lfloor(r-d)^2/4\rfloor\le r^2/3\): putting \(t=r-d\), the bound is \(rt-3t^2/4\le r^2/3\). Since \(r^2/3<2\lfloor r^2/4\rfloor\) for all integers \(r\ge2\), it follows that \(C_r/T_r^2\to0\). For two ideals the nonzero-product probability is \((1+2T_r+T_r^2-C_r)/(T_r+2)^2\to1\), so \(\zeta_2\to0\). For each fixed \(k\ge3\), the nonzero-product numerator is at most \(1+kT_r+\binom{k}{2}T_r^2=O(T_r^2)\), whereas the denominator is asymptotic to \(T_r^k\). Consequently \(\zeta_k\to1\). The rank-two formulas follow by listing the zero, line and full subspaces of a two-space.

## Verification

Run `python3 artifacts/verify.py` after extracting the embedded standalone checker. The checker does **not** assume the ideal classification: it enumerates all row-reduced subspaces of the underlying finite-dimensional algebra and tests ideal closure under multiplication by the radical basis. It then tests direct ideal products for all ordered pairs and triples, comparing with both predicted zero-product counts. Verified results are: rank two over \(\mathbb F_2\), in both alternating and diagonal forms, \(N=7\), with \(25\) zero pairs and \(288\) zero triples; over \(\mathbb F_3\), both hyperbolic and diagonal forms, \(N=8\), \(30\) zero pairs and \(430\) zero triples; over \(\mathbb F_5\), hyperbolic form, \(N=10\), \(40\) zero pairs and \(846\) zero triples; and rank three over \(\mathbb F_2\), diagonal form, \(N=18\), \(101\) zero pairs and \(5213\) zero triples. Output: `VERIFY_OK`. These are finite corroborations; the proof above applies to every allowed ring and prime power.

## Relationship to prior work

Chakraborty and Patra [1] introduce the invariant and provide exact formulas for fields, Boolean rings, chain rings and their finite principal ideal ring products. Their Theorem 4.6 and Corollary 4.7 concern **chain** rings, and their Section 10 explicitly raises universality and further non-chain ring classes as open directions. The present class has \(r\ge2\), so its maximal ideal is not principal; it cannot be a finite chain ring or a product of local chain-ring components. The Gaussian-subspace and orthogonality formulas therefore are not consequences of those enumerations or of direct-product multiplicativity. Related work on short local algebra multiplication tensors [2] concerns monomializability, not the probability distribution of products of randomly chosen ideals. The ideal-lattice and orthogonality reductions use classical finite-vector-space facts, not claimed as new in isolation.

## Limitations

This is a theorem for one natural Gorenstein Loewy-three class, not a characterization of all finite local rings with a Loewy-length-only ideal-product law. The probability depends on \(q\) and \(r\), so it is not universal in Loewy length alone. The asymptotic statement fixes \(r\) and \(k\), and does not address growing embedding dimension or arbitrary socle dimension. The proof is self-contained, but equivalent results framed as orthogonality statistics in an unindexed source remain a bibliographic risk. Independent audit has not been performed.

## References

[1] S. Chakraborty and S. K. Patra, *Ideal Zero-Product Probability in Finite Commutative Rings*, arXiv:2608.14618 (2026), https://arxiv.org/abs/2608.14618 .

[2] *Segre-quadric monomiality criterion for two-generated short local algebras*, published-finding corpus research record, 2026, https://github.com/Resultary/2026 .
