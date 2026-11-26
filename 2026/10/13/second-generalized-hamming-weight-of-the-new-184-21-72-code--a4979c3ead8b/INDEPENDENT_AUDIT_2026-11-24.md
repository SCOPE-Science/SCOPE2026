# Independent mathematical audit

## correctness

PASS

Compared the generator factors, multiplier and the ordered tail patterns with the original arXiv v1 appendix, including its residue convention r_t=Σ_{i≡t mod 5} b_i. An independent reconstruction in /workspace/branches/audit_code184.py uses constant-term polynomial division with exact product verification, cyclic coefficient shifts and binary message doubling rather than the frozen checker's Gray order. Exhausting all 2^21 messages gives positive weight for every nonzero message (hence rank 21), minimum 72 and 9826 minimum words; messages 0x63, 0x318, 0x37b form a minimum triple with union size 108. In every binary two-space each supported coordinate occurs twice among its three nonzero words, so support is at least 3·72/2 and equality holds exactly for triples of minimum words. On the full message space, the ordered count of (u,v) with u,v,u+v in the minimum shell is the sum of the cubes of the unnormalized Walsh transform of its indicator, divided by 2^21, by character orthogonality. The replay gives 3496866 ordered pairs, i.e. 582811 two-spaces since each contributes six. A separate appendix-based direct pair check gives 1748433 unordered pairs, agreeing. This is exact for this code, not a claim about other codes with the same parameters or weights d_r for r≥3.

## originality

PASS

The published construction, minimum distance and shell size are prior inputs. The audited result is the attained second-support bound and exact two-space multiplicity for the specific published generator, not the standard binary support identity or the base code parameters.

## value

PASS

The input is a published high-distance construction and the invariant is the first nontrivial higher generalized weight, not an arbitrary statistic selected after enumeration. The result shows that the universal support lower bound is actually attained and quantifies the minimizing two-spaces. These are precise data for comparing the support geometry of candidate codes and cannot be read from their length, dimension, distance, or ordinary minimum multiplicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
