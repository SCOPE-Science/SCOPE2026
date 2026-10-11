# Independent mathematical audit

## correctness

PASS

The classification proof is correct. Fernandez's Hard Lefschetz condition is equality of the age of a sector and its inverse. Jiang's weighted-projective twisted-sector calculation gives \(\operatorname{age}(e^{2\pi i\theta})=r\theta+\{a\theta\}+\{b\theta\}\). If \(a=b>1\), the primitive \(b\)-th root fixes both heavy coordinates and has ages \(r/b\) and \(r(b-1)/b\), forcing \(b=2\). If \(a<b\), the primitive \(b\)-th root fixes only the \(b\)-coordinate and has age \((r+a)/b\) on a codimension-\(r+1\) sector, so symmetry forces \(2(r+a)=b(r+1)\). For \(a\ge2\), positivity of \(b-a\) together with \(b-a=(2r-a(r-1))/(r+1)\) contradicts its being a positive integer; \(a=1\) gives \(b=2\). The three converse cases have only trivial isotropy or order-two isotropy and satisfy age symmetry. The actual exact checker exhausts \(2\le r\le80\), \(1\le a\le b\le80\); a fresh independent exact inertia sweep for \(2\le r\le11\), \(a,b<20\) found exactly the same three pairs.

## originality

PASS

Fernandez supplies the general age-symmetry criterion and notes that order-two local groups satisfy it, while Jiang supplies the full twisted-sector and degree-shifting machinery for arbitrary weighted projective spaces. Those general decision tools do not classify the infinite family \(\mathbb P(1^r,a,b)\): the audited primitive-largest-weight sector argument turns them into a sharp Diophantine obstruction and proves that no isotropy order above two survives in this family. The inspected sources give general machinery and isolated examples, not the all-\(r,a,b\) classification. Current Resultary search returns the assigned Hard-Lefschetz classification itself as the exact hit; the nearby two-heavy weighted-projective records concern canonicality, Chern ratios, Gorenstein conditions, stabilizers, and other invariants rather than Hard Lefschetz.

## value

PASS

Fernandez's condition is a central structural requirement in orbifold cohomology, and weighted projective stacks are canonical test objects. The theorem gives a complete infinite-family classification rather than checking isolated examples: one primitive sector rules out every higher stabilizer order and leaves exactly three weight pairs in every dimension covered. That is a natural rigidity boundary with a concise structural mechanism, so it clears the common value bar despite the short proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
