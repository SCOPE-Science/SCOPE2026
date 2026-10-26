# Binomial Chern–Schwartz–MacPherson classes of maximal rational-normal secant complements

## Finding
Let \(C_{2r}\subset\mathbb P^{2r}_{\mathbb C}\) be a rational normal curve of degree \(2r\), where \(r\ge1\). Let \(S_r\) be its \(r\)-point secant hypersurface (the closure of the union of \((r-1)\)-planes spanned by length-\(r\) divisors), let \(U_r=\mathbb P^{2r}\setminus S_r\), and put \(H=c_1(\mathcal O_{\mathbb P^{2r}}(1))\). In \(A_*(\mathbb P^{2r})\cong\mathbb Z[H]/(H^{2r+1})\), with the convention that \(H^{2r-i}\) represents \([\mathbb P^i]\), one has for every \(r\ge1\)
\[
 c_{\mathrm{SM}}(\mathbf1_{U_r})
 =\sum_{i=0}^{2r}\binom{r}{\lfloor i/2\rfloor}
     \binom{r}{\lceil i/2\rceil}H^{2r-i}.
\]
Consequently the coefficient functions of fixed dimension index are polynomials in \(r\) of degree at most their index, and the same polynomiality and degree bound holds for every fixed projective degree of the gradient (polar) map of the defining Hankel determinant. This establishes both assertions of Conjecture 4.1 in Nogueira's cited work. The latter conclusion uses the standard Aluffi transformation recalled there; it does not assert that the individual gradient-degree formulas originated here.

## Assumptions and scope
All varieties, Euler characteristics, and Chern–Schwartz–MacPherson classes are over \(\mathbb C\). Fix \(r\in\mathbb Z_{\ge1}\) without any genericity assumption beyond the standard rational normal embedding. Define \(S_0=\varnothing\), and for \(1\le s\le r\), let \(S_s\) denote the locus of binary forms of degree \(2r\) whose border rank is at most \(s\). Thus \(S_s\) has dimension \(2s-1\) and \(S_r\) is the catalecticant hypersurface. The class is pushed forward to the ambient projective space, rather than being an intrinsic class in its Chow group. A class attached to the complement is meant in the constructible-function sense, not the tangent class of a nonexistent compact manifold.

## Proof
**1. The apolar incidence bundle and its fibers.** Let \(W_d=\operatorname{Sym}^d\mathbb C^2\), using the standard duality between degree-\(d\) binary forms and constant-coefficient differential operators. For \(1\le s\le r\), put \(m=2r-s+1\). On \(\mathbb P(W_s)\cong\mathbb P^s\) contraction gives a surjective bundle morphism
\[
 W_{2r}^\vee\otimes\mathcal O\longrightarrow
 W_{2r-s}^\vee\otimes\mathcal O(1).
\]
Indeed its fiber map is dual to multiplication by a nonzero degree-\(s\) binary form and is therefore surjective. Its rank-\(s\) kernel \(E_s\) has projectivization
\[
 B_s=\mathbb P(E_s)=\{([g],[f]):g(\partial)f=0\}
 \subset\mathbb P^s\times\mathbb P^{2r}.
\]
The equations form a regular section of \(\mathcal O(1,1)^{\oplus m}\); hence \(B_s\) is smooth of dimension \(2s-1\), and the second projection \(\pi_s:B_s\to\mathbb P^{2r}\) has image \(S_s\). Write \(T_\ell=S_\ell\setminus S_{\ell-1}\). The classical binary-apolarity complete-intersection description says that the annihilator of a form in \(T_\ell\) has a unique minimal generator of degree \(\ell\), while its other minimal generator has degree \(2r+2-\ell\). Since \(s\le r\), every degree-\(s\) annihilator is a multiple of that first generator. Thus
\[
 \pi_s^{-1}(f)\cong\mathbb P^{s-\ell}
 \quad(f\in T_\ell,\ 1\le\ell\le s),
\]
with the fiber empty off \(S_s\). This agrees with the secant-bundle fiber description \(\operatorname{Sym}^{s-\ell}(\mathbb P^1)\) in Brogan, Proposition 2.3. Proper pushforward of constructible functions therefore gives
\[
 (\pi_s)_*\mathbf1_{B_s}
 =\sum_{\ell=1}^s(s-\ell+1)\mathbf1_{T_\ell}
 =\sum_{\ell=1}^s\mathbf1_{S_\ell}.
\]
In particular \(\mathbf1_{S_r}=(\pi_r)_*\mathbf1_{B_r}-(\pi_{r-1})_*\mathbf1_{B_{r-1}}\), with the last term interpreted as zero when \(r=1\).

**2. Computing the incidence classes.** Let \(h\) and \(H\) be the two hyperplane classes on \(\mathbb P^s\times\mathbb P^{2r}\). The normal bundle of \(B_s\) is \(\mathcal O(1,1)^{\oplus m}\). Adjunction and functoriality of MacPherson classes for proper maps yield
\[
 (\pi_s)_*c_{\mathrm{SM}}(\mathbf1_{B_s})
 =[h^s](1+h)^{s+1}(1+H)^{2r+1}
 \left(\frac{h+H}{1+h+H}\right)^{2r-s+1}.
 \tag{1}
\]
The coefficient \([h^s]\) is the ordinary pushforward along the first projective-space factor; equation (1) is taken modulo \(H^{2r+1}\). Since \(c_{\mathrm{SM}}(\mathbb P^{2r})=(1+H)^{2r+1}\), the constructible-function identity in Step 1 gives
\[
 Q_r(H):=c_{\mathrm{SM}}(\mathbf1_{U_r})
 =(1+H)^{2r+1}\bigl(1-A_r(H)\bigr),
 \tag{2}
\]
where the following rational-function coefficient is expanded at \(h=0\):
\[
 A_r(H)=[h^r]u(h)^r g(h),\quad
 u(h)=\frac{(1+h)(H+h)}{1+H+h}
       =h+\frac H{1+H+h},\quad
 g(h)=\frac{(H+h)(1+H+2h)}{(1+H+h)^2}.
 \tag{3}
\]
The conversion from (1) to (3) is just \([h^{r-1}]F(h)=[h^r]hF(h)\) and the identity
\((1+h)(1+H+h)-h(H+h)=1+H+2h\).

**3. Evaluating the all-degree generating function.** Introduce \(z\), \(a=1+H\), and \(\xi=za^2\). Let \(w=w(\xi)\in\xi\mathbb Q(H)[[\xi]]\) be the unique solution of \(w=\xi u(w)\). The formal residue/Lagrange identity (obtained by taking residues at the formal small root of \(h-\xi u(h)\)) is
\[
 \sum_{r\ge0}\xi^r[h^r]u(h)^r g(h)
 =\frac{g(w)}{1-\xi u'(w)}.
 \tag{4}
\]
The defining equation and \(u(w)=w+H/(a+w)\) imply
\[
 (1-\xi)w(a+w)=\xi H,
 \qquad
 1-\xi u'(w)=\frac{(1-\xi)(a+2w)}{a+w}.
\]
Substituting (3) into (4) gives \(g(w)/(1-\xi u'(w))=(H+w)/((1-\xi)(a+w))\). Equation (2), which also defines the formal value \(Q_0(H)=1\), now gives
\[
 \sum_{r\ge0}z^rQ_r(H)
 =\frac{a}{(1-\xi)(a+w)}
 =\frac{\displaystyle\sqrt{\frac{1-z(H-1)^2}{1-z(H+1)^2}}-1}{2zH}.
 \tag{5}
\]
The radical is the series with constant term one, and the quotient extends regularly to \(H=0\). The quadratic formula for \(w\) proves the last equality; this is a formal series identity, not an analytic branch-choice assumption.

**4. Extracting the binomial coefficients.** Independently define
\[
 R_r(H)=\operatorname{CT}_v(1+v)(H+v)^r(H+v^{-1})^r,
 \tag{6}
\]
where \(\operatorname{CT}\) means the coefficient of \(v^0\). Expanding the two binomials shows that the coefficient of \(H^{2r-i}\) in (6) is exactly \(\binom r{\lfloor i/2\rfloor}\binom r{\lceil i/2\rceil}\). On the other hand, summing (6) over \(r\) gives the constant term of
\((1+v)/(1-z(H+v)(H+v^{-1}))\). Set \(A=1-z(H^2+1)\) and \(B=zH\). The two standard constant-term identities
\[
 \operatorname{CT}_v\frac1{A-B(v+v^{-1})}=
 \frac1{\sqrt{A^2-4B^2}},\qquad
 \operatorname{CT}_v\frac v{A-B(v+v^{-1})}=
 \frac{A/\sqrt{A^2-4B^2}-1}{2B}
\]
show that this generating series equals the right side of (5), since
\(A^2-4B^2=(1-z(H+1)^2)(1-z(H-1)^2)\). Hence \(Q_r(H)=R_r(H)\) for every \(r\ge1\), proving the stated class formula without extrapolation from finite computations.

**5. Consequences for polar degrees.** The binomial products in the theorem are polynomials in \(r\) of degree \(i\) for each fixed \(i\), and they are symmetric in the sense \(c_i(U_r)=c_{2r-i}(U_r)\). Nogueira's Proposition 4.13, based on Aluffi's class/gradient-degree relation and its triangular inversion, states that precisely this symmetry together with the polynomiality of gradient degrees is equivalent to his Conjecture 4.1. One can alternatively use the triangular identity
\[
 c_{2r-i}(U_r)=\sum_{j=0}^i(-1)^j\binom{2r-j}{i-j}d_j(\phi_r),
 \qquad 0\le i\le2r,
\]
to solve successively for each \(d_i(\phi_r)\): the base \(d_0=1\) is constant, and the displayed identity and symmetry make \(d_i\) a polynomial of degree at most \(i\) by induction. Thus both parts of the conjecture hold for every positive integer \(r\).

## Verification
The accompanying standalone Python checker uses a separate projective-bundle Euler-sequence calculation, rather than the formal-residue evaluation, to calculate the pushforwards in (1) with exact integer arithmetic for \(1\le r\le12\). In each case, subtraction of the two incidence classes from the ambient tangent class exactly matches (6). It also checks Euler characteristics and leading classes. Its output ends in `VERIFY_OK`. These tests corroborate, but do not replace, the all-\(r\) proof above.

## Relationship to prior work
Nogueira, *Classes características e secantes de curvas racionais normais*, Chapter 4 (arXiv:2309.09254, first public arXiv version 2023-09-17), explicitly formulates the polynomiality as Conjecture 4.1 and lists the same binomial coefficient prediction in Theorem 4.11 as an equivalence conditional on the conjecture. In particular, that work does **not** prove the all-parameter binomial formula claimed here. Its known low-rank values and first few polar degrees are consistency checks. Brogan, *Invariants of the singularities of secant varieties of curves* (arXiv:2408.16736), Proposition 2.3 and the discussion of secant bundles, supplies a compatible geometric description of the resolution fibers; its paper studies intersection cohomology and vanishing cycles rather than deriving this all-rank CSM formula. General CSM functoriality, adjunction, and Aluffi's transformation are established ingredients and are not claimed as new.

## Limitations
The proof is specific to complex rational normal curves of even ambient degree and the largest proper secant hypersurface. The analogous formula is not asserted for arbitrary curves, other secant codimensions, or characteristic-positive CSM theories. The available comparison cannot exclude an unindexed independent proof or an implicit equivalent calculation in the broader CSM/determinantal literature. Independent mathematical review has not been performed.

## References
- J. R. Nogueira, *Classes características e secantes de curvas racionais normais*, 2020 thesis, arXiv:2309.09254 (first public arXiv posting 2023-09-17), especially Conjecture 4.1, Theorem 4.11 and Proposition 4.13. https://arxiv.org/pdf/2309.09254
- D. Brogan, *Invariants of the singularities of secant varieties of curves*, arXiv:2408.16736 (first posted 2024-08-29), Proposition 2.3 and Section 2. https://arxiv.org/pdf/2408.16736
- P. Aluffi, classical formulas relating Chern–Schwartz–MacPherson classes of hypersurface complements to polar-map projective degrees, as recalled in Nogueira, Section 1.3 and Chapter 4.
- R. MacPherson, natural transformation from constructible functions to homology/Chow characteristic classes, invoked via proper functoriality.
