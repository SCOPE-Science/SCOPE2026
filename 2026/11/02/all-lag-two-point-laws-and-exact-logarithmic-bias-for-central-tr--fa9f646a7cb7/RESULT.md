# All-lag two-point laws and exact logarithmic bias for central trinomial residues modulo five

## Finding

Write \(T_n=[x^0](x^{-1}+1+x)^n\), \(n\ge0\), for the central trinomial coefficients. Their residues modulo five lie in \(G=\mathbb F_5^\times=\{1,2,3,4\}\). For every fixed integer lag \(h\ge0\), there is an **explicitly computable rational probability vector** \(\mu_h:G\to\mathbb Q_{\ge0}\) such that, for every \(u,v\in G\) and every \(N\ge2\),

\[
\#\{0\le n<N:T_n\equiv u,\ T_{n+h}\equiv v\pmod5\}
=\frac{\mu_h(vu^{-1})}{4}N+O_h\bigl((1+\log_5 N)^2\bigr).
\]

The following recursion computes the laws without an infinite limit. Let \(w_0,w_1,w_2,w_3,w_4=(1,1,3,2,4)\). Put \(\mu_0=\delta_1\), \(\mu_1(r)=1/4\) for all \(r\in G\). For \(h\ge2\), write \(h=5q+b\), \(0\le b<5\). For \(a\in\{0,1,2,3,4\}\) define
\[
 j_{a,b}=q+\lfloor(a+b)/5\rfloor,
 \qquad g_{a,b}=w_{(a+b)\bmod5}\,w_a^{-1}\in G.
\]
Then, for \(r\in G\),
\[
 \boxed{\mu_h(r)=\frac15\sum_{a=0}^4\mu_{j_{a,b}}(r g_{a,b}^{-1}).}
\]
Every subscript is strictly less than \(h\), so this is an exact finite algorithm. In particular, adjacent residues are asymptotically independent, since \(\mu_1\) is uniform, while at distance two
\[
 (\mu_2(1),\mu_2(2),\mu_2(3),\mu_2(4))=(1/10,3/10,1/2,1/10),
\]
so distance-two residues are correlated.

More sharply, for each \(k\ge1\), put
\[
 P_k(u,v)=\#\{0\le n<5^k:(T_n,T_{n+1})\equiv(u,v)\pmod5\}.
\]
With
\[
 A=\{(1,1),(1,3),(3,2),(2,4)\},\qquad
 B=\{(4,1),(4,3),(2,2),(3,4)\},
\]
one has the **exact finite-scale identity**
\[
\boxed{P_k(u,v)=\frac{5^k-1}{16}-\frac{k}{4}
+\left\lceil\frac{k}{2}\right\rceil\mathbf1_{(u,v)\in A}
+\left\lfloor\frac{k}{2}\right\rfloor\mathbf1_{(u,v)\in B}
+\mathbf1_{(u,v)=(4^k,1)}.}
\]
The logarithmic deviations at \(N=5^k\) are therefore sharp: they are positive on eight specified ordered pairs and negative on the remaining eight, with bounded additive corrections. This sharpness concerns the finite-level law; the general arbitrary-cutoff bound above is not claimed optimal.

## Assumptions and scope

All congruences are in \(\mathbb F_5\). The integers \(n,h,k,N\) and pairs \(u,v\) have the ranges displayed above. Inverses are multiplicative inverses in \(G\). The constants in the arbitrary-cutoff estimate may depend on fixed \(h\) but are uniform in \(u,v,N\). The distribution \(\mu_h\) is that of the ratio \(T_{n+h}/T_n\) under asymptotic uniform random nonnegative integer \(n\), not a distribution over coefficients of a polynomial.

## Proof

**1. Digit multiplication.** By the freshman's dream,
\[
(x^{-1}+1+x)^{5m+a}\equiv(x^{-5}+1+x^5)^m(x^{-1}+1+x)^a\pmod5
\]
for \(0\le a<5\). The second factor has exponents in \([-4,4]\), whereas the first has exponents divisible by five, so only the product of their constant terms contributes. Consequently
\[
T_{5m+a}\equiv w_aT_m\pmod5,
\qquad (w_0,\ldots,w_4)=(1,1,3,2,4).
\]
Iterating proves that \(T_n\not\equiv0\pmod5\) and that its residue is the product of \(w_a\) across the base-five digits of \(n\).

**2. The ratio recursion and its uniqueness.** For \(h=5q+b\) and \(n=5m+a\), the digit rule gives
\[
\frac{T_{n+h}}{T_n}\equiv g_{a,b}\frac{T_{m+j_{a,b}}}{T_m}\pmod5.
\]
Uniform random base-five digits define a compatible Haar probability law: for any fixed \(h\), adding \(h\) generates only a finite carry string with probability one. The ratio of the corresponding infinite digit products is well defined because all unchanged high digits cancel. Conditioning on the lowest digit gives the displayed recursion.

For \(h=0\), the ratio is one. For \(h=1\), the lowest digits \(a=0,1,2,3\) give the four ratios \(1,3,4,2\) once each; \(a=4\) gives the factor \(4\) times the same tail ratio. Thus \(\mu_1=\frac15\sum_{r\in G}\delta_r+\frac15(4)_*\mu_1\), whose unique probability solution is the uniform law, by contraction of total-variation differences by \(1/5\). If \(h\ge2\), every \(j_{a,b}<h\), which establishes uniqueness, rationality and the finite recursion by induction. The stated \(\mu_2\) follows by substitution.

For a sample of exactly \(5^k\) consecutive indices starting at zero, the first \(k\) digits are independent uniform. If \(n+h<5^k\), the ratio depends only on those digits. Only the final at most \(h\) indices can carry beyond the first \(k\) digits. Coupling the finite and infinite digit processes therefore gives, for each ratio \(r\),
\[
\#\{0\le n<5^k:T_{n+h}/T_n=r\}=5^k\mu_h(r)+O_h(1).
\]
The same assertion holds after applying any multiplicative character of \(G\).

**3. Uniformity of the first residue, even conditioned on a fixed ratio.** Let \(\chi,\psi\) be arbitrary multiplicative characters of \(G\), and write
\[
 F_k(h;\chi,\psi)=\sum_{0\le n<5^k}\chi(T_n)\psi(T_{n+h}).
\]
The digit rule yields the exact identity
\[
 F_k(h;\chi,\psi)=\sum_{a=0}^4\chi(w_a)\psi(w_{(a+b)\bmod5})F_{k-1}(j_{a,b};\chi,\psi).
\]
Suppose \(\chi\psi\ne1\). Since the digit multiset contains one of each nonzero residue plus one extra \(1\), character orthogonality gives
\[
 F_k(0;\chi,\psi)=\left(\sum_{a=0}^4(\chi\psi)(w_a)\right)^k=1.
\]
For \(h=1\), the first four terms in the recursion involve \(F_{k-1}(0)\), and the last term is \(\chi(4)F_{k-1}(1)\), with coefficient of modulus one. Hence \(F_k(1)=O(k+1)\). For \(h\ge2\), all descendant shifts \(j_{a,b}\) are smaller than \(h\); induction on \(h\) gives \(F_k(h)=O_h(k+1)\).

When \(\chi\psi=1\), each summand depends only on the ratio, so the coupling estimate of Step 2 yields
\[
 F_k(h;\chi,\psi)=5^k\sum_{r\in G}\psi(r)\mu_h(r)+O_h(1).
\]
Fourier inversion on \(G\times G\) therefore gives, simultaneously for all \(u,v\in G\),
\[
 \#\{0\le n<5^k:(T_n,T_{n+h})=(u,v)\}
 =\frac{5^k}{4}\mu_h(vu^{-1})+O_h(k+1).
\]

For any integer \(s\ge0\), on the aligned interval \([s5^k,(s+1)5^k)\), except for at most \(h\) final indices, both residues are multiplied by the same nonzero factor \(T_s\). The leading law \(\mu_h(vu^{-1})/4\) is unchanged by this simultaneous multiplication. Thus the same block estimate holds uniformly in \(s\). Every interval \([0,N)\) decomposes into at most four aligned base-five blocks of each length \(5^k\). Summing their \(O_h(k+1)\) errors through \(k\le\lfloor\log_5 N\rfloor\) yields the claimed \(O_h((1+\log_5 N)^2)\) bound.

**4. Exact adjacent-pair counts.** Write \(C_k(u)=\#\{0\le n<5^k:T_n=u\}\). The digit multiset gives
\[
 C_k(u)=(5^k-1)/4+\mathbf1_{u=1}
\]
for all \(k\ge0\). Splitting \(n=5m+a\) shows that each possible ratio \(v/u\) occurs for exactly one \(a\in\{0,1,2,3\}\) and the contribution at \(a=4\) is the old pair scaled in its first coordinate:
\[
 P_k(u,v)=C_{k-1}\bigl(u/w_{a(v/u)}\bigr)+P_{k-1}(u/4,v),
\]
where \(a(1),a(2),a(3),a(4)=(0,3,1,2)\). Iterate this recurrence from \(P_0(u,v)=\mathbf1_{(u,v)=(1,1)}\). The constant contributions sum to \((5^k-1)/16-k/4\). The extra indicator in \(C_{k-j-1}\) alternates between the ordered pair sets \(A\) and \(B\), because \(4^2=1\) in \(G\). The terminal indicator is \((u,v)=(4^k,1)\). Counting the even and odd iterations gives exactly the boxed formula. Since its coefficients of \(k\) are nonzero, logarithmic bias cannot be replaced by a uniform \(O(1)\) estimate at these cutoffs.

## Verification

The standalone `verify_trinomial_5.py` derives central trinomial coefficients independently by their integral three-term recurrence, checks the Lucas digit law for 4,097 indices, tests the exact 16-cell adjacent-pair formula through level 12 by an independent digit-block dynamic program, evaluates 73 exact rational lag distributions, and checks finite ratio statistics on a full base-five block for 39 lags. It also directly enumerates the first six finite adjacent-pair levels. The actual verifier output was:

`VERIFY_OK integer_terms=4097 exact_pair_levels=12 ratio_lags=39 ratio_block=15625 direct_pair_levels=6`

This finite experiment is supporting reproducibility, not the proof for all indices, levels or lags.

## Relationship to prior work

Henningsen and Straub develop Lucas congruences for constant-term sequences; the digit multiplication used here is an instance of that established framework. Straub develops broader constant-term congruence schemes. Kohen studies uniform recurrence and zero-density behavior for generalized central trinomial and related Motzkin sequences. These works supply natural context and important premises but, in the primary material examined, do not state the effective all-lag two-point residue laws, their explicit rational recursion, or the exact 16-cell finite-scale adjacent formula. The OEIS entry for the central trinomial coefficients records the underlying sequence and identities, not a covering two-point theorem.

## Limitations

Only residues modulo five are classified. The constants in the all-lag error term depend on the fixed lag; no uniform-in-lag limit or optimal arbitrary-cutoff discrepancy is asserted. The finite-scale logarithmic bias is proved for cutoffs \(5^k\), not claimed for every cutoff. The originality assessment is restricted to the inspected primary literature, mathematical records and accessible claims; an unindexed or implicit earlier two-point result remains possible. No independent scientific audit has been performed.

## References

1. J. A. Henningsen and A. Straub, *Generalized Lucas congruences and linear p-schemes*, arXiv:2111.08641 (first public 2021-11-16), https://arxiv.org/abs/2111.08641.
2. A. Straub, *On congruence schemes for constant terms and their applications*, arXiv:2205.09902 (first public 2022-05-19), https://arxiv.org/abs/2205.09902.
3. N. Kohen, *Uniform Recurrence in the Motzkin Numbers and Related Sequences mod p*, arXiv:2403.00149 (first public 2024-02-29), https://arxiv.org/abs/2403.00149.
4. OEIS A002426, *Central trinomial coefficients*, https://oeis.org/A002426.
