# Independent mathematical audit

## correctness

PASS

The Gaussian calculation reconstructs exactly. Standardizing the independent fold means gives leave-one-fold-out errors proportional to \(S-Z_i\), so their realized range is the independent-fold range divided by \(B-1\). The vector \((S-Z_i)\) has common variance \(B-1\) and covariance \(B-2\), yielding the stated one-factor equicorrelated-normal integral. Orthogonal decomposition into the grand-mean coordinate and centered residuals gives \(C_B=\mathbb E[\Phi(a_BM_B)-\Phi(a_Bm_B)]\); Taylor expansion at zero together with \(\mathbb E\max Z_i\sim\sqrt{2\log B}\) gives \(C_B\sim2\sqrt{\log B/(\pi B)}\). Independent numerical integration reproduced \(C_2=C_3=1/2\) and \(C_6=0.452918829563530\ldots\), and the bundled verifier's identities were inspected completely.

## originality

PASS

The primary HulC article explicitly assumes independent estimators and constructs them from disjoint data batches; its coverage lemma uses that independence. The audited leave-one-fold-out rule deliberately violates this premise and creates a different equicorrelated Gaussian geometry. Classical orthant-probability theory covers evaluation of the resulting Gaussian event after the covariance is identified, but the exact samplewise \(B-1\) shrinkage together with the HulC coverage-collapse law and its sharp asymptotic were not found in the inspected sources or current Resultary corpus.

## value

PASS

This is a motivated failure boundary for a tempting reuse modification of a modern confidence construction: it proves that a hull can become deterministically narrower while its coverage collapses to zero. The exact finite-sample law and sharp asymptotic quantify the pathology rather than merely warning that independence is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
