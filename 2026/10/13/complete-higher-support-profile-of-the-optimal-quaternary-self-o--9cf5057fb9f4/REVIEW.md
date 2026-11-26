# Independent mathematical audit

## correctness

PASS

For the exact frozen zero set, an independent reproduction formed the ten root factors at a primitive element of F16, verified their coefficients in F4 and checked both cyclicity and Euclidean orthogonality of the five shifted generator rows. Distinct polynomial degrees give rank five. A full-rank generator identifies coefficient subspaces bijectively with subcodes; a coordinate is absent from a subcode precisely when it vanishes on every basis row. The independently written branches/1e887651-99a5-483d-8f22-0c95ba2dfe86/independent_verify.py traversed canonical RREFs in counts 341, 5797, 5797, 341, 1. It recovered all five frozen histograms: (8:15,9:70,11:90,12:70,13:90,15:6); (11:75,12:255,13:990,14:2310,15:2167); (12:5,13:90,14:1080,15:4622); (14:15,15:326); (15:1). Their minima and frequencies match the claim; multiplying one-dimensional frequencies by three, then adding the zero word, gives the weight enumerator. The frozen certificate and relevant verifier logic agree on these checks; the frozen script was not executed. The code specification, rather than an arbitrary code with the same parameters, is what the calculation verifies.

## originality

PASS

Credit the published construction and ordinary parameters, not a new optimal-code claim. The supported distinct result is the full exact subcode-support spectrum of the specified Euclidean cyclic code. The strongest available indexed and literature comparisons do not yield that spectrum. Primary-source access limitations remain explicit.

## value

PASS

This is the full support geometry of a short optimal Euclidean self-orthogonal cyclic representative from an explicit construction, rather than a randomly chosen small code. The minima and multiplicities identify precisely how large message subspaces can be confined to given sets of coordinates, useful for comparing representatives or their shortened codes. For instance, only five three-dimensional subcodes attain support 12, a fact neither the ordinary distance nor the Gaussian totals encode. The complete exact distribution is a meaningful finite invariant without a family-wide optimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
