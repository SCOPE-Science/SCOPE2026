# Same-model review

**Record:** `SCOPE-20260920-1a6f3dc3d0f7`

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof was checked at the level of the hypergeometric normalization, parameter ranges, logarithmic-derivative identities, Riccati residual, endpoint data, and the final exponent comparison.

The key identities are:

1. \(B_b(x)=\sum_{n\ge0} b(b+n)^{-1}x^n\), hence
   \(xB_b'+bB_b=b/(1-x)\).
2. For \(B_*(x)=\operatorname{arctanh}\sqrt{x}/\sqrt{x}\), direct differentiation reduces
   \((1-x)(V+xV^2/2)>1/3\) to \(J(s)>0\). The derivative factorization
   \[
   J'(s)=-2s^{-3}\bigl(3s-(3-s^2)T\bigr)\bigl((3+s^2)T-s\bigr)
   \]
   has the required sign because
   \(T-\frac{3s}{3-s^2}\) has derivative
   \(4s^4/[(1-s^2)(3-s^2)^2]>0\).
3. Coefficientwise \(B_b\le B_{1/2}\) for \(0<b\le1/2\), which through the exact derivative identity gives \(v_b/b\ge2V\).
4. These estimates yield
   \(H_b>(2b^2)/(1+b)\).
5. Substitution of \(z=((1+b)/2)v\) into the Riccati equation for
   \({}_2F_1(1/2,b;1/2+b;x)\) gives exactly
   \[
   \mathcal R=b^2/2-\frac{1+b}{4}H_b<0.
   \]
   The initial logarithmic-derivative gap is
   \(b(1-2b)/(2(2b+1))\ge0\), so a first-crossing argument gives the desired logarithmic-derivative comparison.
6. The coefficient ratio \((a)_n/(a+b)_n\) is increasing in \(a\), extending the result from \(p=2\) to all \(p\ge2\).

No hidden endpoint equality is used: the theorem concerns \(0<r<1\), and all strictness statements are valid there.

## Originality

**PASS, to the best of our knowledge.** The 2019 source explicitly poses equation (33) as an open question. A 2020 paper by Wang and Qi proves a lower bound of the same form with exponent \(1/2\), which does not imply the 2019 exponent throughout \(p,q\ge2\). The present exponent \((q+1)/(2q)\) is stronger than the 2019 requested exponent by
\[
\frac{(p-2)(q-1)}{2pq}.
\]

Searches covered the exact 2019 equation, the source authors/title, \(K_{p,q}\) with \(\operatorname{arctanh}_q\), the new exponent, the hypergeometric reformulation, and later generalized-elliptic literature. No prior statement of this stronger bound was located. The principal residual risk is an equivalent theorem written solely as a zero-balanced hypergeometric inequality or in a poorly indexed source.

## Value

**PASS.** The theorem resolves a concrete named 2019 open inequality and simultaneously strengthens the closest located 2020 lower bound on the full requested parameter region. The proof identifies a reusable mechanism: monotonicity in one hypergeometric parameter reduces the two-parameter problem to an endpoint, and a Riccati comparison transfers a classical \(b=1/2\) logarithmic-derivative estimate to all \(0<b\le1/2\).

## Limitations

- The exponent \((q+1)/(2q)\) is not asserted to be best for fixed \(q\) or fixed \((p,q)\).
- Parameters outside \(p,q\ge2\) are not classified.
- Equivalent prior coverage in substantially different hypergeometric language remains a residual originality risk.
- Independent audit has not been performed.
