# Independent mathematical audit

## correctness

PASS

Fu--Li--Wang--Wang reduce this rational continuous problem exactly to half the discrete Turán problem on \(\{0,\pm1,\pm4,\pm5,\pm6\}\). The package's primal polynomial is the normalized square of a cubic; exact Chebyshev expansion removes every forbidden frequency. The upper certificate uses its three real roots and positive Lagrange-residue weights whose moments at frequencies \(1,4,5,6\) all equal \(-1\); the degree-seven equation for \(a\) makes the final moment and objective equality exact. I independently solved the defining polynomial in the stated interval and reproduced \(a=0.533051836754696\ldots\) and \(\mathcal T_{\mathbb R}=2.135307178876396\ldots\). The inspected checker verifies the polynomial identities and all root/weight signs by exact rational interval arithmetic.

## originality

PASS

The exact same recent source identifies this finite support and proves only the strict lower bound \((559+80\sqrt{42})/506\), explicitly saying that no optimality of the finite problem is claimed. The audited positive three-node dual certificate supplies the missing global upper bound at a different, larger primal value. A fresh Resultary search returns this assigned result as the direct exact match and no earlier set-specific optimum.

## value

PASS

The motivating paper singles out \(\lambda=5/2\) as its first separated rational example beyond the universal value two but leaves the exact finite optimum open. Closing that explicit model with matched primal and positive dual certificates completes a natural endpoint of the paper's reduction program and gives a reusable exact sparse-trigonometric optimization certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
