# Characteristic-two tangent varieties of rational normal curves are smooth scrolls

## Finding

Let \(k\) be algebraically closed of characteristic \(2\), and let \(d\ge3\). For the standard rational normal curve
\[C_d=\{[s^d:s^{d-1}t:\cdots:t^d]\}\subset\mathbb P^d,\]
the reduced closure \(T_d\) of its embedded tangent lines is the smooth rational normal scroll
\[T_d\simeq S(a,b),\qquad a=\lfloor d/2\rfloor,\quad b=\lfloor(d-1)/2\rfloor.\]
Consequently, \(\deg T_d=d-1\). The tangent-incidence parametrization has purely inseparable generic degree \(2\) onto \(T_d\).

## Assumptions and scope

The field is algebraically closed of characteristic exactly \(2\). The embedding is the standard degree-\(d\) rational normal curve in \(\mathbb P^d\), and \(T_d\) is the reduced projective closure of the union of embedded tangent lines. The claim does not identify the scheme-theoretic image of the inseparable incidence morphism, and it makes no assertion for other characteristics or arbitrary embeddings.

## Proof

On the affine chart \(s=1\), write \(p(t)=[1:t:t^2:\cdots:t^d]\). In characteristic \(2\), its derivative is \(p'(t)=[0:1:0:t^2:0:t^4:\cdots]\), since the coefficient \(i\) vanishes for even \(i\) and equals \(1\) for odd \(i\). A point on the tangent line at \(t\) is therefore
\[[1:t+\lambda:t^2:t^3+\lambda t^2:t^4:t^5+\lambda t^4:\cdots].\]
Set \(u=t^2\) and \(v=t+\lambda\). Then every coordinate in range is \(X_{2j}=u^j\) or \(X_{2j+1}=vu^j\).

For \(d=2m\), the even coordinates are \(1,u,\ldots,u^m\) and the odd coordinates are \(v,vu,\ldots,vu^{m-1}\), the standard affine chart of \(S(m,m-1)\). For \(d=2m+1\), both strings run from exponent \(0\) to \(m\), giving \(S(m,m)\). These are the two cases \(S(\lfloor d/2\rfloor,\lfloor(d-1)/2\rfloor)\). Since both indices are positive for \(d\ge3\), the scroll is smooth. Its degree is the sum of its indices, namely \(d-1\).

For the generic degree, the incidence chart has function field \(k(t,\lambda)=k(t,v)\), while the image chart has function field \(k(u,v)=k(t^2,v)\), because \(X_1=v\) and \(X_2=u\). The extension \(k(t,v)/k(t^2,v)\) is nontrivial, purely inseparable, and of degree \(2\). This proves the assertion.

## Verification

The proof uses explicit derivative coordinates, the substitutions \(u=t^2\), \(v=t+\lambda\), the standard affine charts of rational normal scrolls, and a direct function-field degree calculation. The coordinates \(X_1\) and \(X_2\) recover \(v\) and \(u\) for every \(d\ge3\). No finite experiment is used as an infinite proof.

## Relationship to prior work

Ishikawa's 2012 paper classifies generic tangent-variety singularities in smooth real differential geometry; it does not address algebraic images in characteristic \(2\). Kaji's 1989 work develops function-field and ruled-surface methods for inseparable Gauss maps of curves in positive characteristic. This is the closest structural precedent, but the inspected statements do not give the exact parity-dependent scroll type for the standard rational normal curve. Furukawa and Ito's 2014 preprint gives general results on Gauss-map images, fibers, and field extensions, rather than this explicit embedded scroll classification. published-finding corpus searches returned related secant, tangent, and scroll findings but no exact match; that is supporting evidence, not a proof of novelty.

## Limitations

The theorem concerns the reduced image and the generic incidence degree only. It does not determine embedded nilpotents or other scheme-theoretic features of the incidence image, and it is not extended to imperfect fields or characteristics other than \(2\). The literature search is bounded; a general theorem may imply this special case after additional calculation.

## References

1. Goo Ishikawa, “Singularities of Tangent Varieties to Curves and Surfaces,” arXiv:1201.2778, first submitted 13 January 2012. https://arxiv.org/abs/1201.2778
2. Hajime Kaji, “On the Gauss maps of space curves in characteristic \(p\),” *Compositio Mathematica* 70 (1989), 177–197. https://www.numdam.org/articles/CM_1989__70_2_177_0/
3. Katsuhisa Furukawa and Atsushi Ito, “On Gauss maps in positive characteristic in view of images, fibers, and field extensions,” arXiv:1412.7023, first submitted 22 December 2014. https://arxiv.org/abs/1412.7023
4. Joe Harris, *Algebraic Geometry: A First Course*, Graduate Texts in Mathematics 133, Springer, 1992.
