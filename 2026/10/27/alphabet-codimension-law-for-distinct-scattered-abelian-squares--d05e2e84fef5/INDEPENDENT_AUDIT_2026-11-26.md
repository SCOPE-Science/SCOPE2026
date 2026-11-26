# Independent mathematical audit

## correctness

PASS

Greedy waiting times for a fixed string are independent geometric variables by independence of the unread input; the stopping time tests occurrence, not multiplicity of embeddings. The angular constant term enforces exactly q-1 independent Parikh equalities. Strict positivity at consecutive waiting-time degrees rules out a second radial phase at |z|=r, and full support with the last angle fixed forces all angles to be zero in the angular equality case. At the pole in t=z/r the radial derivative is 2 mu, and the quadratic angular defect is theta^T C theta with C=diag(v_1,...,v_{q-1})-vv^T and det C=product v_a. The implicit root is real locally, with log t(theta)=theta^T C theta/(2 mu)+O(|theta|^4). On a fixed sufficiently small angular neighborhood a common circle just outside the roots gives the single residue and a uniform exponentially small remainder; a possibly smaller outside circle works for the complementary compact angular set. Gaussian integration and the analytic factor 1/(1-rt) give the stated constant. Summing unrestricted patterns instead gives U/(1-U); its simple residue gives the ratio of means. In the binary case the cosine integral yields the stated discriminant, and direct algebra gives r=1/(1+s), v_0 v_1=s/(1+2s), mu=2(1+s)/(1+2s). Uniform substitution agrees as well. Checked RESULT.md:20–80, 82–171 and inspected VERIFICATION.md:19–23 and verification.py. The listed finite checks are corroborative and were not rerun; no claim about typical words, varying alphabet, or vanishing masses is validated.

## originality

PASS

The supported distinction is the sharp arbitrary-full-support random-host occurrence law and its weighted constant, not fixed-length Abelian pattern enumeration or the unrestricted subsequence mean. A later indexed binary record gives the same binary marginal and is finer by marking length; it does not cover nonuniform sources of more than two letters. The uniform specialization also follows from prior pattern asymptotics together with the elementary waiting-time mixture, so it is not credited as a separate novelty.

## value

PASS

The statistic combines the natural distinct-subsequence mean with a standard combinatorial symmetry constraint. It quantifies that balance can cost a power for each independent coordinate without altering the exponential base, and specifies the sensitivity to every fixed letter mass. This answers a different quantitative question from counting possible strings or counting unrestricted subsequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
