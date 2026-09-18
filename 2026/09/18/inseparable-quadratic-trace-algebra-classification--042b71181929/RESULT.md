# Inseparable quadratic extensions add a missing family of trace-prime algebras

Let $E/F$ be a quadratic field extension, with no separability assumption, and let $t:E\to E$ be an $F$-linear trace-algebra operation in the sense that
\[
t(ab)=t(ba),\qquad t(a)\in Z(E),\qquad t(t(a)b)=t(a)t(b).
\]
Since $E$ is commutative, the first two conditions are automatic. The remaining axiom admits a complete classification that separates the separable and inseparable cases.

## Theorem

Every such $t$ is exactly one of the following two types:

1. **Multiplication type:**
   \[
   t(x)=\alpha x\qquad(\alpha\in E).
   \]

2. **Scalar-valued type:**
   \[
   t=\ell:E\to F
   \]
   for an arbitrary nonzero $F$-linear functional $\ell\in E^\vee=\operatorname{Hom}_F(E,F)$.

Conversely, every map of either type is a trace-algebra trace.

If $E/F$ is separable, nondegeneracy of the field-trace pairing identifies $E$ with $E^\vee$, so the scalar-valued traces are precisely
\[
\ell_c(x)=\operatorname{Tr}_{E/F}(cx),\qquad c\in E^\times.
\]
If $E/F$ is inseparable, then necessarily $\operatorname{char}F=2$ and the field trace $\operatorname{Tr}_{E/F}$ is identically zero. Hence **none** of the nonzero scalar-valued traces is of the form $x\mapsto\operatorname{Tr}_{E/F}(cx)$.

Thus Lemma 7 of Centrone--Barbosa--Yasumura, arXiv:2609.19797v1, is correct for separable quadratic extensions but is false as stated over an arbitrary field. Their Proposition 11 consequently omits an entire family of two-dimensional tr-prime algebras over nonperfect fields of characteristic $2$.

## Proof

If $t=0$, it is multiplication type with $\alpha=0$. Assume $t\neq0$.

Because $\dim_F E=2$, the image of $t$ has dimension either $1$ or $2$.

If $\dim_F t(E)=2$, then $t$ is surjective. Put $\alpha=t(1)$. For every $x\in E$, choose $y\in E$ with $t(y)=x$. The trace axiom gives
\[
t(x)=t(t(y)\cdot1)=t(y)t(1)=\alpha x.
\]
Hence $t(x)=\alpha x$ for all $x$.

Now suppose $\dim_F t(E)=1$. Choose $u\in E$ with $z:=t(u)\neq0$. Then $t(E)=Fz$. Applying the trace axiom with $a=b=u$ gives
\[
t(zu)=t(t(u)u)=t(u)^2=z^2.
\]
The left-hand side lies in $Fz$, so $z^2=\lambda z$ for some $\lambda\in F$. Since $z\neq0$ and $E$ is a field, $z=\lambda\in F^\times$. Therefore $t(E)=F$, and $t$ is simply a nonzero $F$-linear functional $E\to F$.

Conversely, multiplication maps $x\mapsto\alpha x$ satisfy
\[
t(t(a)b)=\alpha^2ab=t(a)t(b),
\]
and for any $F$-linear $\ell:E\to F$,
\[
\ell(\ell(a)b)=\ell(a)\ell(b),
\]
so every map listed above is a trace-algebra trace.

For a finite field extension, the field-trace pairing
\[
E\times E\longrightarrow F,\qquad (c,x)\longmapsto\operatorname{Tr}_{E/F}(cx)
\]
is nondegenerate exactly when $E/F$ is separable. Hence in the separable quadratic case it realizes every element of $E^\vee$ uniquely as $\ell_c$. In the inseparable case the field trace is identically zero, so this parametrization collapses completely.

## Explicit counterexample

Take
\[
F=\mathbb F_2(s),\qquad E=F(u),\qquad u^2=s.
\]
Since $s$ is not a square in $F$, $E/F$ is a purely inseparable quadratic extension. Define
\[
\ell(a+bu)=b\qquad(a,b\in F).
\]
Then $\ell:E\to F$ is nonzero and $F$-linear, hence
\[
\ell(\ell(x)y)=\ell(x)\ell(y),
\]
so $(E,\ell)$ is a trace algebra. Because the underlying algebra $E$ is a field, it is tr-simple and therefore tr-prime.

On the other hand, $\operatorname{Tr}_{E/F}=0$. Indeed multiplication by $a+bu$ in the basis $(1,u)$ has matrix
\[
\begin{pmatrix}a&bs\\ b&a\end{pmatrix},
\]
whose ordinary matrix trace is $2a=0$. Consequently
\[
\operatorname{Tr}_{E/F}(cx)=0
\]
for every $c,x\in E$, so $\ell$ cannot occur in the field-trace family of Lemma 7. It is also not multiplication type: its image is one-dimensional over $F$, whereas multiplication by a nonzero scalar is surjective and multiplication by zero has zero image.

Thus $(E,\ell)$ is a concrete two-dimensional tr-prime algebra excluded from the four-family list in Proposition 11.

## Corrected arbitrary-field classification

The field-extension part of Proposition 11 can be repaired by replacing its field-trace family with the following:

> For every quadratic field extension $E/F$, include all nonzero scalar-valued traces $\ell\in\operatorname{Hom}_F(E,F)$.

Together with multiplication traces $t_\alpha$, this is exhaustive by the theorem above. For a fixed quadratic extension $E/F$, two scalar-valued trace algebras $(E,\ell)$ and $(E,m)$ are isomorphic exactly when
\[
m=\ell\circ\varphi^{-1}
\]
for some $\varphi\in\operatorname{Aut}_F(E)$. In particular, a purely inseparable quadratic extension has trivial $F$-automorphism group, so **distinct nonzero functionals give pairwise nonisomorphic trace algebras**. Thus the omitted family is not a single exceptional object but the full punctured dual space $E^\vee\setminus\{0\}$ at the level of trace structures and isomorphism classes.

## Scope and downstream impact

The correction concerns the paper's claim to classify two-dimensional tr-prime algebras over an arbitrary field. It does not directly contradict the later finite-base-field classification: finite fields are perfect, so their quadratic extensions are separable and the trace pairing is nondegenerate. Likewise, the explicit finite-field identity bases established later in the paper are not refuted by this counterexample.

The standard separability criterion for the field-trace pairing is classical and is not claimed as new. The new claim here is the identification of the missing inseparable family in arXiv:2609.19797v1, the exact corrected quadratic trace-map classification, and the resulting repair of its arbitrary-field Proposition 11. Originality is to the best of our knowledge. The source preprint is very recent and may be revised.

## References

1. L. Centrone, R. Trindade Barbosa and F. Yasumura, *On the trace identities of 2-dimensional tr-prime algebras over a finite field*, arXiv:2609.19797v1 (2026), especially Lemma 7 and Proposition 11. https://arxiv.org/abs/2609.19797
2. The Stacks Project, Section 9.20, Lemma 9.20.7: a finite field extension is separable if and only if its trace map is nonzero, equivalently if and only if the trace pairing is nondegenerate. https://stacks.math.columbia.edu/tag/0BIE
