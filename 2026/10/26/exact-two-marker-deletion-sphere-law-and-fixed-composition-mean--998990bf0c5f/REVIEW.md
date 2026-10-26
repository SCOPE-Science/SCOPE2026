# Scientific review: exact two-marker deletion spheres

## Correctness — PASS
The proof separates descendant weights two, one and zero, counts retained two-marker gap triples without duplicates, identifies the union of two one-marker position intervals, and double-counts all fixed-weight-two parent/descendant pairs. Discrete coefficientwise balancing establishes an all-length maximizing triple; three extreme deletion allocations force and suffice for the sharp saturation classification. Boundary cases at zero deletions, all deletions and a one-symbol output are explicitly covered. The independent standard-library checker compared 3,003 direct output sets and checked another 1,101,870 finite extremal/plateau cases. Finite checks are not a substitute for the general proof.

## Originality — PASS (with recorded priority uncertainty)
Liron and Langberg (2012, arXiv:1202.1644), especially Lemma II.7, already establish a general deletion-sphere balancing principle: that observation is **not** claimed as new. Hirschberg and Regnier (2000) prove bounds and an average for uniformly random unrestricted-alphabet strings, not the conditional two-marker average. The new assessed contribution is the explicit pointwise gap identity combined with the closed all-radius uniform fixed-weight-two sum, a result not found in the accessed primary material. The related Mercier–Khabbazian–Bhargava (2008) primary text was inaccessible, and it could contain prior equivalent counting consequences. This is a self-review priority assessment, not a guaranteed universal novelty certification.

## Value — PASS
The exact finite-length conditional mean distinguishes fixed-composition deletion outputs from unrestricted-input averages and has an interpretation in binary sparse-source reconstruction and deletion-channel output diversity. The sharp plateau identifies exactly when every possible low-radius deleted-zero allocation and one-marker output is available, and counts **all** maximizers. It exposes a structural fact for an infinite family: for fixed deletion radius, an asymptotic proportion one of weight-two strings attains maximum descendant diversity.

## Closest literature and limitations
Primary comparisons: Liron–Langberg (arXiv:1202.1644, full text in relevant sections) and Hirschberg–Regnier (Journal of Discrete Algorithms 1, 2000, accessible author PDF). The Mercier–Khabbazian–Bhargava 2008 text was not available beyond bibliographic descriptions. The result is restricted to binary linear source strings of weight exactly two and distinct outputs after exactly a specified number of deletions. It does not estimate probabilities of individual outcomes under random deletion locations. Independent scientific audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
