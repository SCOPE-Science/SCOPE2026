# A complete projective classification of smooth plane-filling quintics over the binary field

## Finding
Over \(\mathbb F_2\), exactly \(1512\) homogeneous ternary quintic forms define geometrically smooth plane curves containing all seven points of \(\mathbb P^2(\mathbb F_2)\). Every such curve is geometrically irreducible. Under \(\operatorname{PGL}_3(\mathbb F_2)\) they form exactly ten projective-equivalence classes: eight orbits of length \(168\), and two orbits of length \(84\). Accordingly eight classes have trivial rational projective stabilizer and two have stabilizer of order \(2\).

For clarity, a plane curve defined by \(F\) is *plane-filling* here when \(F(P)=0\) for every \(P\in\mathbb P^2(\mathbb F_2)\). The classification is of **embedded curves under rational projective linear transformations**, not of abstract isomorphism classes over an algebraic closure. Since \(\mathbb F_2^\times=\{1\}\), distinct nonzero homogeneous forms already represent distinct homogeneous equations modulo scalars.

## Assumptions and scope
Let \(V\) be the \(\mathbb F_2\)-vector space of degree-five ternary homogeneous forms vanishing at all seven rational projective points. We quantify over every nonzero member of \(V\), with no restriction on reducibility or singularity prior to testing. Smoothness is geometric, i.e. after extension to \(\overline{\mathbb F}_2\). The primary source published July 6, 2023 studies the natural degree \(q+3\) regime; \(q=2\) is its smallest-field instance.

## Proof
**(1) Enumeration of all plane-filling equations.** Write monomials in the fixed order \(X^iY^jZ^{5-i-j}\), increasing \(i=0,\ldots,5\) and then increasing \(j=0,\ldots,5-i\). There are \(21\) monomials. Evaluation at the seven nonzero binary triples gives seven independent linear constraints: the resulting binary matrix has rank \(7\). Thus \(\dim_{\mathbb F_2}V=14\), and there are \(2^{14}-1=16383\) nonzero candidate forms. The executable code determines a canonical kernel basis by highest-pivot binary elimination and uses its \(14\)-bit coefficient masks to identify forms.

**(2) Certificates for the excluded equations.** For extension degrees \(d=1,\ldots,6\), the code constructs the finite field of order \(2^d\) with exact polynomial arithmetic, examines *all* normalized projective points, and solves the binary linear conditions that the three partial derivatives of \(F\) vanish at that point. Each solution so excluded has an actual geometric singular point. Indeed, Euler's relation reads \(XF_X+YF_Y+ZF_Z=5F=F\) in characteristic two, so vanishing of the gradient implies \(F=0\). The numbers of **newly excluded** equations at successive degrees are, respectively, \(14196,147,24,420,0,84\). Exactly \(1512\) nonzero forms remain. *These bounded field checks alone are not used to assert geometric smoothness*.

**(3) Exact projective orbits.** Generate \(\operatorname{GL}_3(\mathbb F_2)\) by the swaps of the first and second coordinates, of the second and third coordinates, and the transvection \(X\mapsto X+Y\), holding the other two coordinates fixed. These generate all of \(\operatorname{GL}_3(\mathbb F_2)\), which has order \(168\) and equals its projective quotient. Exact polynomial substitution induces permutations of the \(1512\) survivors. Exhausting each orbit gives the following ten representatives, displayed using the coefficient-mask convention in step (1):

| Mask | Orbit size | Representative polynomial over \(\mathbb F_2\) |
|---:|---:|---|
| `157` | 168 | \(Y Z^4 + Y^3 Z^2 + X Z^4 + X Y Z^3 + X Y^4 + X^3 Y Z + X^4 Z + X^4 Y\) |
| `159` | 168 | \(Y Z^4 + Y^2 Z^3 + Y^3 Z^2 + Y^4 Z + X Z^4 + X Y Z^3 + X Y^4 + X^3 Y Z + X^4 Z + X^4 Y\) |
| `174` | 84 | \(Y^2 Z^3 + Y^3 Z^2 + X Z^4 + X Y^2 Z^2 + X Y^4 + X^3 Y Z + X^4 Z + X^4 Y\) |
| `251` | 168 | \(Y Z^4 + Y^2 Z^3 + X Z^4 + X Y Z^3 + X Y^2 Z^2 + X Y^3 Z + X Y^4 + X^3 Y Z + X^4 Z + X^4 Y\) |
| `410` | 84 | \(Y^2 Z^3 + Y^4 Z + X Z^4 + X Y Z^3 + X Y^4 + X^2 Z^3 + X^3 Y Z + X^4 Y\) |
| `413` | 168 | \(Y Z^4 + Y^3 Z^2 + X Z^4 + X Y Z^3 + X Y^4 + X^2 Z^3 + X^3 Y Z + X^4 Y\) |
| `417` | 168 | \(Y Z^4 + Y^4 Z + X Y^2 Z^2 + X Y^4 + X^2 Z^3 + X^3 Y Z + X^4 Z + X^4 Y\) |
| `433` | 168 | \(Y Z^4 + Y^4 Z + X Y Z^3 + X Y^2 Z^2 + X Y^4 + X^2 Z^3 + X^4 Z + X^4 Y\) |
| `463` | 168 | \(Y Z^4 + Y^2 Z^3 + Y^3 Z^2 + Y^4 Z + X Z^4 + X Y^3 Z + X Y^4 + X^2 Z^3 + X^3 Y Z + X^4 Y\) |
| `684` | 168 | \(Y^3 Z^2 + Y^4 Z + X Z^4 + X Y^2 Z^2 + X Y^4 + X^2 Y Z^2 + X^4 Z + X^4 Y\) |

The orbit sizes sum to \(8\cdot168+2\cdot84=1512\); no other surviving forms exist.

**(4) Algebraic-closure smoothness, independently of the extension cutoff.** For each of the ten polynomials displayed above, exact Gröbner-basis computation over \(\mathbb F_2\) shows that the three partial derivatives generate the unit ideal on **each** of the affine charts \(X=1\), \(Y=1\), and \(Z=1\). Thus none has any geometric common gradient zero. This proves geometric smoothness of every representative, and of all \(1512\) forms in their projective orbits. Combining steps (2) and (4) proves completeness. A smooth projective plane curve cannot split into positive-degree components over an algebraically closed field, by Bézout, hence each listed quintic is geometrically irreducible.

**(5) Stabilizers.** The orbit-stabilizer theorem in the order-168 group gives stabilizers of sizes \(1\) and \(2\), respectively, and no others occur.

## Verification
Run `python3 verify.py` using Python 3 and SymPy. The program exhausts all \(16384\) masks (including the zero mask only for linear-algebra bookkeeping), computes every extension-field singularity witness through degree \(6\), re-enumerates the ten group orbits, and verifies the ten Gröbner unit ideals on all three affine charts. It also verifies irreducibility of the six selected field moduli. The main computed checkpoints are \(1512\) smooth curves and the multiset of orbit lengths \(\{84,84,168,168,168,168,168,168,168,168\}\). The full computation was executed and passed using the attached program, not inferred from a sample.

## Relationship to prior work
Asgarli--Ghioca [1] introduce and investigate the \(q+3\) plane-filling regime and specific constructed families, but their results inspected here do not enumerate all binary quintics, their rational projective orbits, or rational stabilizer sizes. Homma--Kim [2] classify the distinct minimal-degree \(q+2\) problem, which at \(q=2\) concerns quartics, not the present quintics. The quoted ten-orbit classification is not implied by the existence or formulae for specific \(q+3\) examples. A targeted search of published mathematical records, the available earlier classification records, and the primary literature did not reveal a covering census; this is a best-knowledge novelty assessment rather than an exhaustive historical theorem.

## Limitations
Only quintics over \(\mathbb F_2\) are classified, and only up to \(\operatorname{PGL}_3(\mathbb F_2)\), not up to arbitrary abstract curve isomorphism. The intermediate extension-degree cutoff \(d\le6\) is a technique for *witnessing singularities*, not a presumed degree bound for all geometric singular points; final smoothness uses the full unit-ideal certificates. The symbolic proof of each chart unit ideal relies on reproducible exact Gröbner calculations. Older literature may contain equivalent tabulations not located by the performed searches.

## References
[1] Shamil Asgarli and Dragos Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1 (first public release 2023-07-06), https://arxiv.org/abs/2307.03072.

[2] Masaaki Homma and Seon Jeong Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups: Supplements to a work of Tallini*, arXiv:0903.1918 (first released 2009-03-11), https://arxiv.org/abs/0903.1918.
