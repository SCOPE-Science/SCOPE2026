# Weddle quartic point-count distributions over the two smallest characteristic-two fields

## Finding
For \(q=8\), all 120 projective classes of **ordered**, linearly general six-point configurations in \(\mathbb P^3(\mathbb F_q)\) have associated Weddle quartics with exactly 145 rational points. For \(q=16\), the complete point-count distribution is

| \(\#W(\mathbb F_{16})\) | Number of ordered-frame classes |
|---:|---:|
| 417 | 1440 |
| 433 | 144 |
| 449 | 600 |

There are 2184 such classes in total. These are actual point counts on the singular quartic, **not** on its minimal desingularization. The distinction between the three arithmetic strata at \(q=16\) already occurs at the first extension field after the smallest admissible one.

## Assumptions and scope
All fields have characteristic two. Label six projective points and require that no four of them lie in a plane. A unique projectivity takes the first five points to \([1:0:0:0]\), \([0:1:0:0]\), \([0:0:1:0]\), \([0:0:0:1]\), and \([1:1:1:1]\). The remaining point is \([1:b:c:d]\), with \(b,c,d\) pairwise distinct elements of \(\mathbb F_q\setminus\{0,1\}\). Thus the parameter count is \((q-2)(q-3)(q-4)\). This determines **ordered configurations modulo projective transformations**, not unlabelled sets or abstract surface isomorphism classes. Such a configuration exists over \(\mathbb F_q\) exactly when the field has at least six elements; \(8\) and \(16\) are the first two powers of two for which that occurs.

For \((a,b,c,d)=(1,b,c,d)\), Dolgachev's Weddle equation is the vanishing of the determinant
\[
\det\begin{pmatrix}
ayzw&x&1&a\\ bxzw&y&1&b\\ cxyw&z&1&c\\ dxyz&w&1&d
\end{pmatrix}.
\]

## Proof
1. The first-five-points normal form is an ordered projective frame, so the normalizing projectivity is unique. For the sixth point, exclusion from planes spanned by triples among the first five is equivalent to all four entries being nonzero and pairwise unequal. Scaling \(a\) to one yields precisely the parameters stated above, without duplication.

2. In characteristic two, direct determinant expansion is the homogeneous quartic
\[
\begin{aligned}
F_{a,b,c,d}={}&ab wz(w+z)(x+y)+ac wy(w+y)(x+z)\\
&+ad yz(y+z)(w+x)+bc wx(w+x)(y+z)\\
&+bd xz(x+z)(w+y)+cd xy(x+y)(w+z).
\end{aligned}
\]
The identity is an integer-polynomial identity after reduction modulo two; it is checked symbolically independently of the census. The attached program also compares the determinant with the expanded quartic at every projective point for one representative from each resulting count class.

3. Represent elements of \(\mathbb F_8\) as binary residues modulo \(t^3+t+1\), and elements of \(\mathbb F_{16}\) modulo \(t^4+t+1\). Both moduli are irreducible over \(\mathbb F_2\): the former has no binary roots; the latter has neither a binary root nor the degree-two irreducible factor \(t^2+t+1\). Addition is bitwise XOR and multiplication is the explicitly implemented modular polynomial product.

4. Each projective point has exactly one vector whose first nonzero entry is \(1\). Enumerating first-nonzero indices \(0,1,2,3\), followed by arbitrary entries to the right, lists \(q^3+q^2+q+1\) projective points, without duplicates or omissions. For each ordered parameter triple, evaluate \(F\) at every one of those points and count the zeros. Enumerating all injections of length three into \(\mathbb F_q\setminus\{0,1\}\) enumerates **all** ordered frames, without samples. This is a finite exhaustive proof with exact arithmetic, not statistical extrapolation.

5. The resulting exact histograms, printed and asserted by `verify.py`, are \(\{145:120\}\) at \(q=8\) and \(\{417:1440,433:144,449:600\}\) at \(q=16\). Their multiplicities sum respectively to \(120\) and \(2184\), independently matching the frame count.

## Verification
Run `python3 verify.py`; it requires only the Python 3 standard library. Successful completion prints `VERIFY_OK`, along with both histograms, and checks the complete determinant directly against the expanded quartic at all rational projective points for at least one representative of each count. The program's exhaustive loops and finite-field routines are contained in this package. A separate symbolic polynomial expansion showed that all coefficients of the determinant-minus-expanded-quartic vanish modulo two.

## Relationship to prior work
Dolgachev, *K3 surfaces of Kummer type in characteristic two*, Section 2, supplies the six-point normal form, quartic determinant and the geometric interpretation of these Weddle surfaces, including the extra characteristic-two \(D_4\) singularity. This work addresses a different finite-field arithmetic question: the **complete distribution** of rational-point counts among coordinate-normalized ordered six-point configurations over the first two permissible fields. No such histogram was identified in the inspected source or targeted comparisons. Classical and unindexed finite-field tabulations remain an originality risk; nonappearance in searches is not a uniqueness proof.

## Limitations
The enumerations apply only to \(q=8\) and \(q=16\), not larger fields or all field extensions. They are counts of projective rational points of the singular quartic, not zeta functions, geometric isomorphism classes, or minimal-resolution point counts. The finite checker is exhaustive for the stated fields; it is not an infinite-field argument. The relationship between the three count classes and a structural moduli-theoretic invariant is not determined here. Independent validation has not been performed.

## References
- I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, arXiv:2302.13101v1 (first publicly posted 2023-02-25), especially Section 2, equation (2), and Proposition 2.1. https://arxiv.org/abs/2302.13101
- I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, *Bulletin of the London Mathematical Society*, DOI:10.1112/blms.13033 (full-text version, Section 2).
