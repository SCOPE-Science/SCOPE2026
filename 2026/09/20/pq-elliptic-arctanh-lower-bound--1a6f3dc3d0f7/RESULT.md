# A stronger lower bound for complete \((p,q)\)-elliptic integrals

**Record ID:** `SCOPE-20260920-1a6f3dc3d0f7`

## Main result

Let \(p,q\ge 2\) and \(0<r<1\). With the standard generalized complete elliptic integral
\[
K_{p,q}(r)=\frac{\pi_{p,q}}2\,{}_2F_1\!\left(1-\frac1p,\frac1q;1-\frac1p+\frac1q;r^q\right)
\]
and
\[
\operatorname{arctanh}_q(r)
=r\,{}_2F_1\!\left(1,\frac1q;1+\frac1q;r^q\right),
\]
one has the strict inequality
\[
\boxed{\;
K_{p,q}(r)>
\frac{\pi_{p,q}}2
\left(\frac{\operatorname{arctanh}_q(r)}{r}\right)^{\frac{q+1}{2q}}
\; }.
\]

This is stronger than the open inequality posed as Remark 5, equation (33), by Dou, Yin and Lin (2019), whose exponent is
\[
\frac{p+q-1}{pq}.
\]
Indeed
\[
\frac{q+1}{2q}-\frac{p+q-1}{pq}
=\frac{(p-2)(q-1)}{2pq}\ge0,
\]
and \(\operatorname{arctanh}_q(r)/r>1\). Thus the 2019 open question has an affirmative answer.

For comparison, Wang and Qi (2020) proved the lower bound with exponent \(1/2\) for \(p\ge2,\ q>1\). The exponent above is strictly larger than \(1/2\) for every finite \(q\ge2\). At \(p=q=2\) it becomes \(3/4\), exactly the sharp classical Alzer--Qiu exponent.

## Hypergeometric form

Put
\[
a=1-\frac1p,\qquad b=\frac1q,\qquad x=r^q.
\]
Then \(a\in[1/2,1)\), \(b\in(0,1/2]\), and it is enough to prove
\[
{}_2F_1(a,b;a+b;x)
>
{}_2F_1(1,b;1+b;x)^{(1+b)/2}.
\tag{1}
\]

Write
\[
A_a(x)={}_2F_1(a,b;a+b;x),\qquad
B_b(x)={}_2F_1(1,b;1+b;x),
\qquad d=\frac{1+b}{2}.
\]

### Step 1: reduction to \(a=1/2\)

For every \(n\ge1\),
\[
\frac{(a)_n}{(a+b)_n}
=\prod_{k=0}^{n-1}\frac{a+k}{a+b+k}
\]
is strictly increasing in \(a\), because
\[
\frac{d}{da}\log\frac{(a)_n}{(a+b)_n}
=\sum_{k=0}^{n-1}
\frac{b}{(a+k)(a+b+k)}>0.
\]
All coefficients in the hypergeometric series are positive. Hence, for \(x\in(0,1)\),
\[
A_a(x)\ge A_{1/2}(x).
\]
It remains to show
\[
A_{1/2}(x)>B_b(x)^d.
\tag{2}
\]

### Step 2: a logarithmic-derivative lemma at \(b=1/2\)

Let
\[
B_*(x)=B_{1/2}(x)
=\frac{\operatorname{arctanh}\sqrt{x}}{\sqrt{x}},
\qquad
V(x)=\frac{B_*'(x)}{B_*(x)}.
\]
Then
\[
\boxed{\;
(1-x)\left(V(x)+\frac{x}{2}V(x)^2\right)>\frac13
\qquad(0<x<1).
\;}
\tag{3}
\]

To prove this, put \(s=\sqrt{x}\) and \(T=\operatorname{arctanh}s\). Direct simplification gives
\[
(1-x)\left(V+\frac{x}{2}V^2\right)-\frac13
=
\frac{J(s)}{24T^2(1-s^2)},
\]
where
\[
J(s)=3-(1-s^2)
\left[
(9-s^2)\left(\frac{T}{s}\right)^2
-6\frac{T}{s}
\right].
\]
Moreover,
\[
J'(s)
=-\frac{2}{s^3}
\bigl(3s-(3-s^2)T\bigr)
\bigl((3+s^2)T-s\bigr).
\]
The second factor is positive. For the first factor, define
\[
Q(s)=T-\frac{3s}{3-s^2}.
\]
Then \(Q(0+)=0\) and
\[
Q'(s)=\frac{4s^4}{(1-s^2)(3-s^2)^2}>0.
\]
Thus \(3s-(3-s^2)T<0\), so \(J'(s)>0\). Since \(J(0+)=0\), (3) follows.

### Step 3: transfer the lemma to every \(0<b\le1/2\)

The elementary series
\[
B_b(x)=\sum_{n=0}^{\infty}\frac{b}{b+n}x^n
\]
shows coefficientwise that
\[
B_b(x)\le B_{1/2}(x)=B_*(x).
\tag{4}
\]
It also gives the exact identity
\[
xB_b'(x)+bB_b(x)=\frac{b}{1-x}.
\]
If \(v=B_b'/B_b\), then
\[
\frac{v}{b}
=
\frac1x\left(\frac1{(1-x)B_b(x)}-1\right)
\ge 2V.
\tag{5}
\]

Define
\[
H_b(x)=(1-x)\left(v+(1-b)xv^2\right).
\]
Set
\[
P=(1-x)V,\qquad
R=(1-x)xV^2.
\]
By (5),
\[
H_b
\ge 2bP+4b^2(1-b)R.
\]
Since \(4b(1-b)\le1\),
\[
2bP+4b^2(1-b)R
\ge
8b^2(1-b)\left(P+\frac R2\right).
\]
Using (3),
\[
H_b>
\frac83 b^2(1-b).
\]
Finally \(b\le1/2\) implies \(4(1-b^2)\ge3\), hence
\[
\boxed{\;
H_b(x)>\frac{2b^2}{1+b}.
\;}
\tag{6}
\]

### Step 4: Riccati comparison

Let
\[
w=\frac{A_{1/2}'}{A_{1/2}},
\qquad
v=\frac{B_b'}{B_b},
\qquad
z=dv,\qquad d=\frac{1+b}{2}.
\]
The hypergeometric differential equations give
\[
x(1-x)(w'+w^2)
+\left[b+\frac12-\left(b+\frac32\right)x\right]w
-\frac b2=0,
\tag{7}
\]
and
\[
x(1-x)(v'+v^2)
+\left[b+1-(b+2)x\right]v
-b=0.
\tag{8}
\]
Substituting \(z=dv\) into the left side of (7) and using (8) yields the exact residual
\[
\mathcal R(x)
=
\frac{b^2}{2}
-\frac d2\,H_b(x).
\]
By (6), \(\mathcal R(x)<0\).

Now put \(\Delta=w-z\). Subtracting the Riccati equations gives
\[
x(1-x)\Delta'
+
\left[
x(1-x)(w+z)
+b+\frac12-\left(b+\frac32\right)x
\right]\Delta
=-\mathcal R(x)>0.
\tag{9}
\]
At the origin,
\[
\Delta(0)
=
\frac{b}{2b+1}-\frac b2
=
\frac{b(1-2b)}{2(2b+1)}
\ge0.
\]
Equation (9) rules out a downward crossing of \(\Delta\) through zero; moreover \(\Delta\) cannot vanish identically because \(\mathcal R<0\). Consequently
\[
\frac{d}{dx}
\left(\log A_{1/2}-d\log B_b\right)
=\Delta\ge0
\]
and the derivative is not identically zero. Since both logarithms vanish at \(x=0\), (2) follows strictly for \(x>0\).

Combining Step 1 with Step 4 proves (1), hence the stated \((p,q)\)-elliptic inequality.

## Relation to the 2019 open problem

Dou, Yin and Lin asked whether
\[
K_{p,q}(r)>
\frac{\pi_{p,q}}2
\left(\frac{\operatorname{arctanh}_q(r)}r\right)^{(p+q-1)/(pq)}
\qquad(p,q\ge2)
\]
holds. The theorem above proves the stronger exponent \((q+1)/(2q)\). Equality of the two exponents occurs exactly at \(p=2\); for \(p>2\) the new lower bound is strictly stronger.

## Literature check and originality scope

- Dou, Yin and Lin (2019), Remark 5, equation (33), explicitly pose the target inequality as an open question.
- Wang and Qi (2020), Theorem 1.2(1), prove the same type of lower bound with exponent \(1/2\) for \(p\ge2,\ q>1\).
- The classical \(p=q=2\) exponent \(3/4\) is the sharp Alzer--Qiu bound.
- Searches using the named 2019 problem, the exact exponent \((p+q-1)/(pq)\), the stronger exponent \((q+1)/(2q)\), the hypergeometric formulation, and combinations of \(K_{p,q}\) with \(\operatorname{arctanh}_q\) did not locate a prior result establishing the bound above.

The originality claim is therefore only **to the best of our knowledge**. A differently phrased or poorly indexed hypergeometric inequality could still provide prior coverage.

## Limitations

1. The exponent \((q+1)/(2q)\) is not claimed to be optimal for fixed \(q\) (or fixed \(p,q\)); the proof is aimed at closing the 2019 question with a clean stronger bound.
2. The parameter range proved here is \(p,q\ge2\). No claim is made about the same exponent outside that range.
3. The literature search cannot exclude an equivalent result stated in substantially different hypergeometric notation.
4. Independent audit has not been performed.

## References

1. X. Dou, L. Yin, X.-L. Lin, “Functional Inequalities for Generalized Complete Elliptic Integrals with Two Parameters,” *Journal of Function Spaces* (2019), Article 4752856. https://doi.org/10.1155/2019/4752856
2. F. Wang, F. Qi, “Monotonicity and sharp inequalities related to complete \((p,q)\)-elliptic integrals of the first kind,” *Comptes Rendus Mathématique* 358 (2020), 961–970. https://doi.org/10.5802/crmath.119
3. H. Alzer, S.-L. Qiu, “Monotonicity theorems and inequalities for the complete elliptic integrals,” *Journal of Computational and Applied Mathematics* 172 (2004), 289–312. https://doi.org/10.1016/j.cam.2004.02.009

**Same-model review: passed. Independent audit: not yet performed.**
